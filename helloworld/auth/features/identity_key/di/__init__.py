from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncSession

from helloworld.core.services.decorators import service_manager
from helloworld.auth.features.identity_key.data import IdentityKeyRepository
from helloworld.auth.features.identity_key import IdentityKeyRepositoryImpl

@service_manager("database", "auth")
async def get_identity_key_repository(session: AsyncSession, authorization: str | None = None) -> IdentityKeyRepository:
    return IdentityKeyRepositoryImpl(session, authorization)