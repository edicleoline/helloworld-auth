from __future__ import annotations

from datetime import datetime

from helloworld.core import BaseEntity, Field

class IdentityVerificationEntity(BaseEntity):
    identity_id: int = Field(title="Identity Id")
    target_id: int = Field(title="Target Id")
    verification_type: str = Field(title="Target type", min_length=1, max_length=10)
    created_at: datetime = Field(default_factory=datetime.now, title="Created At")