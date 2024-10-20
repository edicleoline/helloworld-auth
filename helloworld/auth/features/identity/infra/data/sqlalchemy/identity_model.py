from __future__ import annotations

from datetime import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from helloworld.core.infra.data.sqlalchemy import BaseModel
from helloworld.auth.features.identity import IdentityEntity

class IdentityModel(BaseModel[IdentityEntity]):
    __tablename__ = "identity"
    __entity_cls__ = IdentityEntity

    username: Mapped[str] = mapped_column(String(50), nullable=True)
    email: Mapped[str] = mapped_column(String(256), nullable=True, unique=True)
    phone: Mapped[str] = mapped_column(String(20), nullable=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=True)
    last_login: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
