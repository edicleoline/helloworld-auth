from __future__ import annotations

from helloworld.core.data import AbstractUnitOfWork
from helloworld.core.phoning import CallService
from helloworld.core.services.service_manager import service_manager

from ...entities.device_otp_request_entity import DeviceOTPRequestEntity
from ...otp_strategy import OTPStrategy

class CallOTPStrategy(OTPStrategy):
    def __init__(self, unit_of_work: AbstractUnitOfWork):
        super().__init__(unit_of_work)

    async def send(self, request: DeviceOTPRequestEntity) -> None:
        call_service: CallService = service_manager.get("phoning", "call")
        await call_service.send(
            to=request.phone_number,
            priority=request.priority,
            template=request.template,
            lang=request.lang,
            code=request.code,
            **request.params
        )