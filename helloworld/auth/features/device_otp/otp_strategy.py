from __future__ import annotations

from abc import ABC, abstractmethod

from helloworld.core.data import AbstractUnitOfWork
from .entities.device_otp_request_entity import DeviceOTPRequestEntity

class OTPStrategy(ABC):
    def __init__(self, unit_of_work: AbstractUnitOfWork):
        self.unit_of_work = unit_of_work

    @abstractmethod
    async def send(self, otp_request: DeviceOTPRequestEntity):
        pass