from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Any

class AbstractService(ABC):
    secret_key: str
    algorithm: str
    expiration_minutes: int
    iss: str

    def init(self, secret_key: str, algorithm: str = "HS256", expiration_minutes: int = 15, iss: str = "helloworld"):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.expiration_minutes = expiration_minutes
        self.iss = iss

    @abstractmethod
    async def encode(self, data: Dict[str, Any]) -> str:
        raise NotImplementedError

    @abstractmethod
    async def decode(self, token: str) -> Dict[str, Any] | None:
        raise NotImplementedError