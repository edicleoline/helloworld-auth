from __future__ import annotations

from typing import Optional

from helloworld.core import BaseEntity, Field

class IdentityKeyEntity(BaseEntity):
    identity_id: Optional[int] = Field(None, title="Identity Id")
    token: Optional[str] = Field(None, title="Key")