from __future__ import annotations

from datetime import datetime, timezone
from typing import Tuple
from abc import ABC

from helloworld.core import BaseUseCaseUnitOfWork
from helloworld.auth.features.otp import OTPRequestEntity
from helloworld.auth.features.otp.data import OTPRequestRepository
from helloworld.auth.error import exceptions as auth_exceptions
from helloworld.auth.jwt.services import TokenService
from helloworld.auth.features.otp.const import SUB

class ValidateUseCase(BaseUseCaseUnitOfWork[Tuple[str, str], OTPRequestEntity], ABC):
    async def execute(self, token: str, code: str) -> bool:
        raise NotImplementedError

class ValidateUseCaseImpl(ValidateUseCase):
    async def execute(self, token: str, code: str) -> bool:
        async with self.unit_of_work as unit_of_work:
            token_service: TokenService = await self.services.get("authentication", "otp-token")
            decoded_token = await token_service.decode(token)

            if not decoded_token:
                raise auth_exceptions.InvalidTokenError

            sub = decoded_token.get(SUB)

            otp_req_repository: OTPRequestRepository = await unit_of_work.repository_factory \
                .instance(OTPRequestRepository)

            otp_req_entity = await otp_req_repository.find(id=sub)

            if not otp_req_entity or otp_req_entity.verified_at:
                return False

            valid = otp_req_entity.code == code

            if valid:
                otp_req_entity.verified_at = datetime.now(timezone.utc)
                await otp_req_repository.save(otp_req_entity)

            return valid