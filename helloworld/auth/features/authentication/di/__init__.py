from __future__ import annotations

from helloworld.core.data import AbstractUnitOfWork, get_unit_of_work
from helloworld.auth.features.authentication import IdentifyUseCase, IdentifyUseCaseImpl
from helloworld.auth.features.authentication import AuthenticateUseCase, AuthenticateUseCaseImpl

async def get_identify_use_case(unit_of_work: AbstractUnitOfWork | None = None, authorization: str | None = None) -> IdentifyUseCase:
    unit_of_work = get_unit_of_work(authorization) if not unit_of_work else unit_of_work
    return IdentifyUseCaseImpl(unit_of_work, authorization)

async def get_authenticate_use_case(unit_of_work: AbstractUnitOfWork | None = None, authorization: str | None = None) -> AuthenticateUseCase:
    unit_of_work = get_unit_of_work(authorization) if not unit_of_work else unit_of_work
    return AuthenticateUseCaseImpl(unit_of_work, authorization)