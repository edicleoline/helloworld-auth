from __future__ import annotations

from abc import ABC
from datetime import datetime
from typing import Any

from helloworld.core import BaseUseCaseUnitOfWork
from helloworld.auth.features.identity import IdentityRepository
from helloworld.auth.features.jwt.services import AbstractService
from helloworld.core.util.security import verify_password, hash_password
from helloworld.auth.features.authentication.entities import ResponseEntity

class AuthenticateUseCase(BaseUseCaseUnitOfWork[dict[str, Any], ResponseEntity], ABC):
    async def execute(self, token: str, **kwargs) -> ResponseEntity | None:
        raise NotImplementedError

class AuthenticateUseCaseImpl(AuthenticateUseCase):
    async def execute(self, token: str, **kwargs) -> ResponseEntity | None:
        async with self.unit_of_work as unit_of_work:
            identity_repository: IdentityRepository = await unit_of_work.repository_factory.instance(IdentityRepository)

            token_jwt_service: AbstractService = await self.services.get("authentication", "token")
            decoded_token = await token_jwt_service.decode(token)

            if not decoded_token or not decoded_token.get("sub") or not decoded_token.get("opt") or not decoded_token.get("method"):
                raise ValueError("Invalid token.")

            sub = decoded_token.get("sub")
            opt = decoded_token.get("opt")
            method = decoded_token.get("method")

            password = kwargs.get("password")

            identity_entity = await identity_repository.find(id=sub)

            if not identity_entity:
                raise ValueError

            is_oneshot_signin = opt == "signin" and (method == "email" or method == "username")
            is_oneshot_signup = opt == "signup" and (method == "email" or method == "username")

            if not password and (is_oneshot_signin or is_oneshot_signup):
                raise Exception("password necessary")

            if is_oneshot_signin and identity_entity.password_hash and not verify_password(password, identity_entity.password_hash):
                raise ValueError

            if is_oneshot_signup or (is_oneshot_signin and (not identity_entity.password_hash or verify_password(password, identity_entity.password_hash))):
                # todo: security layer. suspended user?

                updated_identity = identity_entity.copy(
                    password_hash=hash_password(password) if not identity_entity.password_hash else identity_entity.password_hash,
                    last_login=datetime.now()
                )
                identity_entity = await identity_repository.save(updated_identity)

                refresh_token_jwt_service: AbstractService = await self.services.get("authentication", "refresh-token")

                access_token = await token_jwt_service.encode({"sub": identity_entity.id})
                refresh_token = await refresh_token_jwt_service.encode({"sub": identity_entity.id})

                # if is_oneshot_signup and identity_entity.email:
                #     from helloworld.core.mailing.services import MailingService
                #     mailing_service: MailingService = await self.services.get("mailing", "public")
                #     await mailing_service.send(
                #         template="welcome",
                #         lang="pt",
                #         priority="critical",
                #         to=identity_entity.email,
                #         subject="welcome",
                #         first_name="João"
                #     )

                return ResponseEntity(access_token=access_token, refresh_token=refresh_token)

            raise NotImplementedError("Others methods (phone or oauth2) not implemented yet.")