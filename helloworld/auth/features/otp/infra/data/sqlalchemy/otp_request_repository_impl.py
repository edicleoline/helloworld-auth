from __future__ import annotations

from typing import overload

from sqlalchemy.ext.asyncio import AsyncSession

from helloworld.auth.features.otp import OTPRequestEntity
from helloworld.auth.features.otp.data import OTPRequestRepository
from helloworld.core.infra.data.sqlalchemy import BaseRepository
from .otp_request_model import OTPRedquestModel

class OTPRequestRepositoryImpl(OTPRequestRepository, BaseRepository[OTPRequestEntity, OTPRedquestModel]):
    def __init__(self, session: AsyncSession, authorization: str | None = None):
        super().__init__(session=session, model_cls=OTPRedquestModel, authorization=authorization)

    @overload
    async def find(self, id: int) -> OTPRequestEntity | None: ...

    @overload
    async def find(self, token: str) -> OTPRequestEntity | None: ...

    async def find(self, *args, **kwargs) -> OTPRequestEntity | None:
        if "id" in kwargs:
            return await self._find(id=kwargs['id'])
        elif 'token' in kwargs:
            return await self._find(token=kwargs['token'])
        else:
            raise ValueError("You must provide either 'id' or 'token' as a keyword argument.")
