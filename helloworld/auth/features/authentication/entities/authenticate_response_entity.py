from __future__ import annotations

from pydantic import BaseModel, Field

class AuthenticateResponseEntity(BaseModel):
    access_token: str = Field(title="Access token")
    refresh_token: str = Field(title="Refresh token")