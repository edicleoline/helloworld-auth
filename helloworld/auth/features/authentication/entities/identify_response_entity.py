from __future__ import annotations

from pydantic import BaseModel, Field

class IdentifyResponseEntity(BaseModel):
    access_token: str = Field(title="Access token")
    redirect: str = Field(title="Flow")