from __future__ import annotations

from abc import ABC
from typing import overload

from helloworld.core.data import AbstractRepository, TModel
from helloworld.auth.features.otp import OTPRequestEntity

class OTPRequestRepository(AbstractRepository[OTPRequestEntity, TModel], ABC):
    @overload
    async def find(self, id: int) -> OTPRequestEntity | None: ...

    @overload
    async def find(self, token: str) -> OTPRequestEntity | None: ...

    async def find(self, *args, **kwargs):
        raise NotImplementedError