from __future__ import annotations

from abc import ABC
from datetime import datetime
from typing import Any

from helloworld.core import BaseUseCaseUnitOfWork
from helloworld.core.util.security import verify_password, hash_password
from helloworld.core.util.arguments import get_kwarg
from helloworld.auth.features.identity.data import IdentityRepository
from helloworld.auth.jwt.services import TokenService
from helloworld.auth.features.authentication.entities import AuthenticateResponseEntity
from helloworld.auth.error import exceptions
from helloworld.account.features.user import UserEntity
from helloworld.account.features.user.data import UserRepository
from helloworld.core.error.exceptions import InvalidRequestError

class RefreshTokenteUseCase(BaseUseCaseUnitOfWork[dict[str, Any], AuthenticateResponseEntity], ABC):
    async def execute(self, token: str, **kwargs) -> AuthenticateResponseEntity | None:
        raise NotImplementedError

class RefreshTokenUseCaseImpl(RefreshTokenteUseCase):
    async def execute(self, token: str, **kwargs) -> AuthenticateResponseEntity | None:
        async with self.unit_of_work as unit_of_work:
            token_service: TokenService = await self.services.get("authentication", "token")
            refresh_token_service: TokenService = await self.services.get("authentication", "refresh-token")

            decoded_token = await refresh_token_service.decode(token)

            if not decoded_token or not decoded_token.get("sub"):
                raise exceptions.InvalidTokenError(f"Invalid token {token}.")

            sub = decoded_token.get("sub")

            access_token = await token_service.encode({"sub": sub})
            refresh_token = await refresh_token_service.encode({"sub": sub})

            return AuthenticateResponseEntity(access_token=access_token, refresh_token=refresh_token)