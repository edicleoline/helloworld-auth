from __future__ import annotations

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from helloworld.core.infra.data.sqlalchemy import BaseModel
from helloworld.auth.features.identity_key import IdentityKeyEntity

class IdentityKeyModel(BaseModel[IdentityKeyEntity]):
    __tablename__ = "identity_key"
    __entity_cls__ = IdentityKeyEntity

    id: Mapped[str] = mapped_column(primary_key=True)
    identity_id: Mapped[str] = mapped_column(String(80))
    token: Mapped[str] = mapped_column(String(540))
