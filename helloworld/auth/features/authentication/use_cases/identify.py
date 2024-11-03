from __future__ import annotations

from abc import ABC

from helloworld.core import BaseUseCaseUnitOfWork
from helloworld.core.util import is_valid_phone, is_valid_email
from helloworld.auth.features.identity import IdentityEntity
from helloworld.auth.features.identity.data import IdentityRepository
from helloworld.auth.features.identity_key import IdentityKeyRepository, IdentityKeyEntity
from helloworld.auth.jwt.services import TokenService
from helloworld.account.features.user import UserEntity
from helloworld.account.features.user.data import UserRepository
from helloworld.auth.features.authentication.entities import IdentifyResponseEntity

async def find_identity(repository: IdentityRepository, identifier: str) -> IdentityEntity | None:
    fields = ["username", "email", "phone"]
    for field in fields:
        identity = await repository.find(**{field: identifier})
        if identity:
            return identity
    return None

class IdentifyUseCase(BaseUseCaseUnitOfWork[str, IdentifyResponseEntity | None], ABC):
    async def execute(self, identifier: str) -> IdentifyResponseEntity | None:
        raise NotImplementedError

class IdentifyUseCaseImpl(IdentifyUseCase):
    async def execute(self, identifier: str) -> IdentifyResponseEntity | None:
        async with self.unit_of_work as unit_of_work:
            identity_repository: IdentityRepository = await unit_of_work.repository_factory.instance(IdentityRepository)
            identity_entity = await find_identity(identity_repository, identifier)

            method = ("phone" if is_valid_phone(identifier) else "email" if is_valid_email(identifier) else "username")
            token_data = {"opt": "signup" if not identity_entity else "signin", "method": method, "scope": ["read"]}

            user_repository: UserRepository = await unit_of_work.repository_factory.instance(UserRepository)
            user_entity: UserEntity | None = await user_repository.find(identity_id=identity_entity.id) if identity_entity else None

            redirect = "/auth/password" if method in {"email", "username"} and identity_entity and identity_entity.password_hash else "/auth/register"

            if method == "phone":
                redirect = 'phone/verify'

            if (
                method in {"email", "username"}
                and identity_entity
                and identity_entity.email
                and identity_entity.last_login
                and not identity_entity.password_hash
                and user_entity
            ):
                raise NotImplementedError("Password reset flow for users with an existing identity and last login but "
                                          "without a password hash is not implemented.")

            if not identity_entity:
                identity_entity = await identity_repository.save(IdentityEntity(**{method: identifier}))

            token_service: TokenService = await self.services.get("authentication", "token")
            token_data["sub"] = identity_entity.id

            token = await token_service.encode(token_data)

            identity_key_repository: IdentityKeyRepository = await unit_of_work.repository_factory.instance(IdentityKeyRepository)

            await identity_key_repository.save(IdentityKeyEntity(
                identity_id=identity_entity.id,
                token=token
            ))

            return IdentifyResponseEntity(access_token=token, redirect=redirect)