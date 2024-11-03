from __future__ import annotations

from typing import Dict, Any
from pydantic import BaseModel, Field

from helloworld.core.queuing import Priority
from ..types import OTPType

class DeviceOTPRequestEntity(BaseModel):
    otp_type: OTPType = Field(title="Type")
    code: str = Field(title="Code")
    phone_number: str | None = Field(title="Phone")
    priority: Priority = Field(title="Priority")
    template: str = Field(title="Template")
    lang: str = Field(title="Language")
    params: Dict[str, Any] = Field(default_factory=dict, title="Additional Parameters")