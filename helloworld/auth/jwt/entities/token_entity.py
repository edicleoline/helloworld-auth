from __future__ import annotations

from typing import Optional

from helloworld.core import BaseEntity, Field

class TokenEntity(BaseEntity):
    username: Optional[str] = Field(None, title="Username", min_length=1, max_length=240)
    email: Optional[str] = Field(None, title="Email", min_length=1, max_length=240)
    phone: Optional[str] = Field(None, title="Phone", min_length=1, max_length=240)
    password_hash: Optional[str] = Field(None, title="Passwd", min_length=1, max_length=540)