from __future__ import annotations

from typing import overload

from sqlalchemy.ext.asyncio import AsyncSession

from helloworld.core.data.repositories.abstract_repository import LogicalOperator
from helloworld.auth.features.identity import IdentityEntity
from helloworld.auth.features.identity.data import IdentityRepository
from helloworld.account.features.user import UserEntity

from .identity_model import IdentityModel
from helloworld.core.infra.data.sqlalchemy import BaseRepository

class IdentityRepositoryImpl(IdentityRepository, BaseRepository[IdentityEntity, IdentityModel]):
    def __init__(self, session: AsyncSession, authorization: str | None = None):
        super().__init__(session=session, model_cls=IdentityModel, authorization=authorization)

    @overload
    async def find(self, username: str) -> UserEntity | None:
        return await self._find(username=username)

    @overload
    async def find(self, email: str) -> UserEntity | None:
        return await self._find(email=email)

    @overload
    async def find(self, phone: str) -> UserEntity | None:
        return await self._find(phone=phone)

    async def find(self, criteria: LogicalOperator = "and", **kwargs) -> IdentityEntity | None:
        return await self._find_criteria(criteria, **kwargs)
