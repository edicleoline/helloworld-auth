from __future__ import annotations

from sqlalchemy import String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from helloworld.core.infra.data.sqlalchemy import BaseModel
from helloworld.auth.features.identity_key import IdentityKeyEntity

class IdentityKeyModel(BaseModel[IdentityKeyEntity]):
    __tablename__ = "identity_key"
    __entity_cls__ = IdentityKeyEntity

    identity_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    token: Mapped[str] = mapped_column(String(255), nullable=False)
