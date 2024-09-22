from __future__ import annotations

from helloworld.auth.features.identity_key import IdentityKeyEntity
from helloworld.auth.features.identity_key.data import IdentityKeyRepository
from .identity_key_model import IdentityKeyModel
from helloworld.core.infra.data.sqlalchemy import BaseRepository

from sqlalchemy.ext.asyncio import AsyncSession

class IdentityKeyRepositoryImpl(IdentityKeyRepository, BaseRepository[IdentityKeyEntity, IdentityKeyModel]):
    def __init__(self, session: AsyncSession, authorization: str | None = None):
        super().__init__(session=session, model_cls=IdentityKeyModel, authorization=authorization)