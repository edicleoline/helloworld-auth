from __future__ import annotations

from enum import Enum

class OTPType(Enum):
    SMS = "sms"
    CALL = "call"
    MISSED_CALL = "missed_call"
    APP = "app"
    EMAIL = "email"

    @classmethod
    def from_string(cls, value: str) -> OTPType:
        try:
            return cls[value.upper()]
        except KeyError:
            raise ValueError(f"'{value}' is not a valid OTPType")