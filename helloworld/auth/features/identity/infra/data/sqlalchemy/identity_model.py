from __future__ import annotations

from datetime import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from helloworld.core.infra.data.sqlalchemy import BaseModel
from helloworld.auth.features.identity import IdentityEntity

class IdentityModel(BaseModel[IdentityEntity]):
    __tablename__ = "identity"
    __entity_cls__ = IdentityEntity

    id: Mapped[str] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(80))
    email: Mapped[str] = mapped_column(String(240))
    phone: Mapped[str] = mapped_column(String(240))
    password_hash: Mapped[str] = mapped_column(String(540))
    last_login: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
