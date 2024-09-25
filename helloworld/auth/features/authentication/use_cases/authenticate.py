from __future__ import annotations

from abc import ABC
from datetime import datetime
from typing import Any

from helloworld.core import BaseUseCaseUnitOfWork
from helloworld.core.util.security import verify_password, hash_password
from helloworld.core.util.arguments import get_kwarg
from helloworld.auth.features.identity import IdentityRepository
from helloworld.auth.jwt.services import AbstractService
from helloworld.auth.features.authentication.entities import ResponseEntity
from helloworld.auth.error import exceptions
from helloworld.account.features.user import UserEntity
from helloworld.account.features.user.data import UserRepository
from helloworld.core.error.exceptions import InvalidRequestError

class AuthenticateUseCase(BaseUseCaseUnitOfWork[dict[str, Any], ResponseEntity], ABC):
    async def execute(self, token: str, **kwargs) -> ResponseEntity | None:
        raise NotImplementedError

class AuthenticateUseCaseImpl(AuthenticateUseCase):
    async def execute(self, token: str, **kwargs) -> ResponseEntity | None:
        async with self.unit_of_work as unit_of_work:
            token_service: AbstractService = await self.services.get("authentication", "token")
            decoded_token = await token_service.decode(token)

            if not decoded_token or not decoded_token.get("sub") or not decoded_token.get("opt") or not decoded_token.get("method"):
                raise exceptions.InvalidTokenError(f"Invalid token {token}.")

            sub = decoded_token.get("sub")
            opt = decoded_token.get("opt")
            method = decoded_token.get("method")

            password = kwargs.get("password")

            identity_repository: IdentityRepository = await unit_of_work.repository_factory.instance(IdentityRepository)
            identity_entity = await identity_repository.find(id=sub)

            if not identity_entity:
                raise InvalidRequestError(f"There is no identity for sub {sub}.")

            user_repository: UserRepository = await unit_of_work.repository_factory.instance(UserRepository)
            user_entity: UserEntity | None = await user_repository.find(identity_id=identity_entity.id)

            kwuser = get_kwarg(kwargs, "user", UserEntity)
            if not user_entity:
                if not kwuser:
                    raise InvalidRequestError(f"Signup mode: you have to tell me about user. Use 'user' argument.")

                user_entity_copy = kwuser.copy(id = None, identity_id=identity_entity.id)
                user_entity = await user_repository.save(user_entity_copy)

            is_oneshot_signin = opt == "signin" and method in {"email", "username"}
            is_oneshot_signup = opt == "signup" and method in {"email", "username"}

            if not password and (is_oneshot_signin or is_oneshot_signup):
                raise InvalidRequestError("You have to tell me the password.")

            if is_oneshot_signin and identity_entity.password_hash and not verify_password(password, identity_entity.password_hash):
                raise exceptions.InvalidLoginOrPasswordError("Invalid login or password.")

            if is_oneshot_signup or (is_oneshot_signin and (not identity_entity.password_hash or verify_password(password, identity_entity.password_hash))):
                updated_identity = identity_entity.copy(
                    password_hash=hash_password(password) if not identity_entity.password_hash else identity_entity.password_hash,
                    last_login=datetime.now()
                )

                identity_entity = await identity_repository.save(updated_identity)

                refresh_token_service: AbstractService = await self.services.get("authentication", "refresh-token")

                access_token = await token_service.encode({"sub": identity_entity.id})
                refresh_token = await refresh_token_service.encode({"sub": identity_entity.id})

                return ResponseEntity(access_token=access_token, refresh_token=refresh_token)

            raise NotImplementedError("Support for other authentication methods (e.g., phone or OAuth2) has not been implemented yet.")