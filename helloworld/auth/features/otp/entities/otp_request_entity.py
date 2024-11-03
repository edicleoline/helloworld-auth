from __future__ import annotations

from datetime import datetime
from helloworld.core.domain.entities.base_entity import BaseEntity, Field

class OTPRequestEntity(BaseEntity):
    code: str = Field(title="Code", min_length=4, max_length=20)
    token: str = Field(title="Token", min_length=15, max_length=255)
    created_at: datetime = Field(default_factory=datetime.now, title="Created At")
    verified_at: datetime | None = Field(default=None, title="Verified At")
