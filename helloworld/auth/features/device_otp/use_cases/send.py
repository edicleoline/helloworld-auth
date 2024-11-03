from __future__ import annotations

from abc import ABC

from helloworld.auth.features.device_otp import DeviceOTPRequestEntity
from helloworld.core import BaseUseCaseUnitOfWork
from helloworld.core.data import AbstractUnitOfWork
from helloworld.auth.features.device_otp import OTPType
from helloworld.auth.features.device_otp.otp_strategy import OTPStrategy

class SendUseCase(BaseUseCaseUnitOfWork[DeviceOTPRequestEntity, None], ABC):
    async def execute(self, request: DeviceOTPRequestEntity) -> None:
        raise NotImplementedError

class SendUseCaseImpl(SendUseCase):
    def __init__(self, strategies: dict[OTPType, OTPStrategy], unit_of_work: AbstractUnitOfWork, authorization: str | None = None):
        super().__init__(unit_of_work, authorization)
        self.strategies = strategies

    async def execute(self, request: DeviceOTPRequestEntity) -> None:
        async with self.unit_of_work as unit_of_work:
            strategy = self.strategies.get(request.otp_type)
            await strategy.send(request)