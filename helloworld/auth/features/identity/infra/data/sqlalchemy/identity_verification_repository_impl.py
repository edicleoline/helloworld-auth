from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncSession

from helloworld.auth.features.identity import IdentityVerificationEntity
from helloworld.auth.features.identity.data import IdentityVerificationRepository
from helloworld.core.data.repositories.abstract_repository import LogicalOperator

from .identity_verification_model import IdentityVerificationModel
from helloworld.core.infra.data.sqlalchemy import BaseRepository

class IdentityVerificationRepositoryImpl(IdentityVerificationRepository, BaseRepository[IdentityVerificationEntity, IdentityVerificationModel]):
    def __init__(self, session: AsyncSession, authorization: str | None = None):
        super().__init__(session=session, model_cls=IdentityVerificationModel, authorization=authorization)

    async def find(self, criteria: LogicalOperator = "and", **kwargs) -> IdentityVerificationEntity | None:
        return await self._find_criteria(criteria, **kwargs)