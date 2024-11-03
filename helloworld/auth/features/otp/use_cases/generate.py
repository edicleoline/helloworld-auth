from __future__ import annotations

from typing import Tuple, Dict, Union
from abc import ABC

from helloworld.core import BaseUseCaseUnitOfWork
from helloworld.auth.features.otp import OTPRequestEntity
from helloworld.auth.features.otp.data import OTPRequestRepository
from helloworld.auth.jwt.services import TokenService
from helloworld.auth.features.otp.const import SUB

class GenerateUseCase(BaseUseCaseUnitOfWork[Tuple[Dict[str, Union[str, int]], str], OTPRequestEntity], ABC):
    async def execute(self, data: Dict[str, Union[str, int]], code: str) -> OTPRequestEntity:
        raise NotImplementedError

class GenerateUseCaseImpl(GenerateUseCase):
    async def execute(self, data: Dict[str, Union[str, int]], code: str) -> OTPRequestEntity:
        async with self.unit_of_work as unit_of_work:
            otp_request_id = OTPRequestEntity.new_id()
            data[SUB] = otp_request_id

            token_service: TokenService = await self.services.get("authentication", "otp-token")
            token = await token_service.encode(data)

            otp_request_repository: OTPRequestRepository = await unit_of_work.repository_factory.instance(OTPRequestRepository)

            return await otp_request_repository.create(OTPRequestEntity(
                id = otp_request_id,
                code = code,
                token = token,
            ))