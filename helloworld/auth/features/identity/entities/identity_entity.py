from __future__ import annotations

from typing import Optional
from datetime import datetime

from helloworld.core import BaseEntity, Field, constr

class IdentityEntity(BaseEntity):
    username: Optional[constr(
        strip_whitespace=True,
        pattern=r'^[A-Za-z0-9_]+$',
        min_length=1,
        max_length=45
    )] = Field(None, title="Username")

    email: Optional[str] = Field(None, title="Email", min_length=1, max_length=240)
    phone: Optional[str] = Field(None, title="Phone", min_length=1, max_length=240)
    password_hash: Optional[str] = Field(None, title="Passwd", min_length=1, max_length=540)
    last_login: Optional[datetime] = Field(None, title="Last login")