from __future__ import annotations

from helloworld.core.data import AbstractUnitOfWork
from helloworld.core.phoning import SMSService
from helloworld.core.services.service_manager import service_manager

from ...entities.device_otp_request_entity import DeviceOTPRequestEntity
from ...otp_strategy import OTPStrategy

class SMSOTPStrategy(OTPStrategy):
    def __init__(self, unit_of_work: AbstractUnitOfWork):
        super().__init__(unit_of_work)

    async def send(self, request: DeviceOTPRequestEntity) -> None:
        sms_service: SMSService = service_manager.get("phoning", "sms")
        await sms_service.send(
            to=request.phone_number,
            lang=request.lang,
            template=request.template,
            priority=request.priority,
            code=request.code,
            **request.params
        )