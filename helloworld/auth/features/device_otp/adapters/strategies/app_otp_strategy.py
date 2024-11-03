from __future__ import annotations

from helloworld.core.data import AbstractUnitOfWork
from helloworld.core.notification import NotificationService
from helloworld.core.services.service_manager import service_manager

from ...entities.device_otp_request_entity import DeviceOTPRequestEntity
from ...otp_strategy import OTPStrategy

class APPOTPStrategy(OTPStrategy):
    def __init__(self, unit_of_work: AbstractUnitOfWork):
        super().__init__(unit_of_work)

    async def send(self, request: DeviceOTPRequestEntity) -> None:

        device_id = 123456

        service: NotificationService = service_manager.get("notification", "main")
        await service.send(
            device_id=device_id,
            lang=request.lang,
            title="someone request login",
            template=request.template,
            code=request.code,
            priority=request.priority,
            payload_data={"url": "/test"},
            **request.params
        )