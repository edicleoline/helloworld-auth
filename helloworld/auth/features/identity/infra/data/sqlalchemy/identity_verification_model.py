from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import String, DateTime, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from helloworld.core.infra.data.sqlalchemy import BaseModel
from helloworld.auth.features.identity import IdentityVerificationEntity

class IdentityVerificationModel(BaseModel[IdentityVerificationEntity]):
    __tablename__ = "identity_verification"
    __entity_cls__ = IdentityVerificationEntity

    identity_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    target_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    verification_type: Mapped[str] = mapped_column(String(10), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc),
                                                 nullable=False)
