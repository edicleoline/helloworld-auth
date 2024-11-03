from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from helloworld.core.infra.data.sqlalchemy import BaseModel
from helloworld.auth.features.otp import OTPRequestEntity

class OTPRedquestModel(BaseModel[OTPRequestEntity]):
    __tablename__ = "otp_request"
    __entity_cls__ = OTPRequestEntity

    code: Mapped[str] = mapped_column(String(20), nullable=False)
    token: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    verified_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
