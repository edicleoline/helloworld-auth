from __future__ import annotations

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from typing import Any, Dict

import jwt

from helloworld.auth.jwt.services import TokenService

class JWTService(TokenService):
    async def encode(self, data: Dict[str, Any]) -> str:
        expiration_time = datetime.now(tz=ZoneInfo('UTC')) + timedelta(minutes=self.expiration_minutes)
        payload = {
            **data,
            "iss": self.iss,
            "exp": expiration_time
        }
        token = jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
        return token

    async def decode(self, token: str) -> Dict[str, Any] | None:
        try:
            decoded_data = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return decoded_data
        except jwt.ExpiredSignatureError:
            print("Expired token", "/home/edicleo/dev/helloworld/backend/libs/auth/helloworld/auth/jwt/services/jwt_service.py")
        except jwt.InvalidTokenError:
            print("Invalid token")

        return None