from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncSession

from helloworld.core.data import AbstractUnitOfWork, get_unit_of_work
from helloworld.core.services.decorators import service_manager
from helloworld.auth.features.otp.data import (OTPRequestRepository, OTPRequestRepositoryImpl, OTPRequestLimitRepository,
                                               OTPRequestLimitRepositoryImpl)
from helloworld.auth.features.otp.use_cases import GenerateUseCase, GenerateUseCaseImpl, ValidateUseCase, ValidateUseCaseImpl

@service_manager("database", "auth")
async def get_otp_request_repository(session: AsyncSession, authorization: str | None = None) -> OTPRequestRepository:
    return OTPRequestRepositoryImpl(session, authorization)

async def get_generate_use_case(unit_of_work: AbstractUnitOfWork | None = None, authorization: str | None = None) -> GenerateUseCase:
    unit_of_work = get_unit_of_work(authorization) if not unit_of_work else unit_of_work
    return GenerateUseCaseImpl(unit_of_work, authorization)

@service_manager("database", "auth")
async def get_otp_request_limit_repository(session: AsyncSession, authorization: str | None = None) -> OTPRequestLimitRepository:
    return OTPRequestLimitRepositoryImpl(session, authorization)

async def get_validate_use_case(unit_of_work: AbstractUnitOfWork | None = None, authorization: str | None = None) -> ValidateUseCase:
    unit_of_work = get_unit_of_work(authorization) if not unit_of_work else unit_of_work
    return ValidateUseCaseImpl(unit_of_work, authorization)