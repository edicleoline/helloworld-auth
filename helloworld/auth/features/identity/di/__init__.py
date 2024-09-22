from __future__ import annotations

from helloworld.core.services.decorators import service_manager
from helloworld.auth.features.identity.data import IdentityRepository, IdentityRepositoryImpl

from sqlalchemy.ext.asyncio import AsyncSession

@service_manager("database", "auth")
async def get_identity_repository(session: AsyncSession, authorization: str | None = None) -> IdentityRepository:
    return IdentityRepositoryImpl(session, authorization)