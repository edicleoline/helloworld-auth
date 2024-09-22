from __future__ import annotations

from abc import ABC

from helloworld.core import BaseUseCaseUnitOfWork
from helloworld.auth.features.identity import IdentityRepository, IdentityEntity
from helloworld.auth.features.identity_key import IdentityKeyRepository, IdentityKeyEntity
from helloworld.core.util import is_valid_phone, is_valid_email
from helloworld.auth.jwt.services import AbstractService

async def find_identity(repository: IdentityRepository, identifier: str) -> IdentityEntity | None:
    fields = ["username", "email", "phone"]
    for field in fields:
        identity = await repository.find(**{field: identifier})
        if identity:
            return identity
    return None

class IdentifyUseCase(BaseUseCaseUnitOfWork[str, str], ABC):
    async def execute(self, identifier: str) -> str | None:
        raise NotImplementedError

class IdentifyUseCaseImpl(IdentifyUseCase):
    async def execute(self, identifier: str) -> str | None:
        async with self.unit_of_work as unit_of_work:
            identity_repository: IdentityRepository = await unit_of_work.repository_factory.instance(IdentityRepository)
            identity_entity = await find_identity(identity_repository, identifier)

            method = ("phone" if is_valid_phone(identifier) else "email" if is_valid_email(identifier) else "username")
            token_data = {"opt": "signup" if not identity_entity else "signin", "method": method, "scope": ["read"]}

            if identity_entity and identity_entity.last_login and not identity_entity.password_hash:
                if method == "email":
                    print("Send email to reset password")
                elif method == "username":
                    print("Impossible")

                return None

            if not identity_entity:
                identity_entity = await identity_repository.save(IdentityEntity(**{method: identifier}))

            jwt_service: AbstractService = await self.services.get("authentication", "token")
            token_data["sub"] = identity_entity.id

            token = await jwt_service.encode(token_data)

            identity_key_repository: IdentityKeyRepository = await unit_of_work.repository_factory.instance(IdentityKeyRepository)

            await identity_key_repository.save(IdentityKeyEntity(
                identity_id=identity_entity.id,
                token=token
            ))

            return token