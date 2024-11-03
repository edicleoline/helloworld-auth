from __future__ import annotations

from helloworld.core.data import AbstractUnitOfWork, get_unit_of_work
from helloworld.auth.features.device_otp import OTPType
from helloworld.auth.features.device_otp.otp_strategy import OTPStrategy
from helloworld.auth.features.device_otp.use_cases.send import SendUseCase, SendUseCaseImpl
from helloworld.auth.features.device_otp.adapters.strategies import SMSOTPStrategy, CallOTPStrategy, MissedCallOTPStrategy, APPOTPStrategy

async def get_strategies(unit_of_work: AbstractUnitOfWork | None = None, authorization: str | None = None) -> dict[OTPType, OTPStrategy]:
    unit_of_work = get_unit_of_work(authorization) if not unit_of_work else unit_of_work
    return {
        OTPType.SMS: SMSOTPStrategy(unit_of_work),
        OTPType.CALL: CallOTPStrategy(unit_of_work),
        OTPType.MISSED_CALL: MissedCallOTPStrategy(unit_of_work),
        OTPType.APP: APPOTPStrategy(unit_of_work)
    }

async def get_send_use_case(unit_of_work: AbstractUnitOfWork | None = None, authorization: str | None = None) -> SendUseCase:
    unit_of_work = get_unit_of_work(authorization) if not unit_of_work else unit_of_work
    strategies = await get_strategies(unit_of_work, authorization)
    return SendUseCaseImpl(strategies, unit_of_work, authorization)