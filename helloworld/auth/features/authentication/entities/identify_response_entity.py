from __future__ import annotations

from pydantic import BaseModel, Field

class IdentifyResponseEntity(BaseModel):
    access_token: str = Field(title="Access token")
    method: str = Field(title="Identify method")