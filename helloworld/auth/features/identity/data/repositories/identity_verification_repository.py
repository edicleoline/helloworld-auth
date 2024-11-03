from __future__ import annotations

from abc import ABC
from typing import overload

from helloworld.core.data import AbstractRepository, TModel
from helloworld.auth.features.identity import IdentityVerificationEntity
from helloworld.core.data.repositories.abstract_repository import LogicalOperator

class IdentityVerificationRepository(AbstractRepository[IdentityVerificationEntity, TModel], ABC):
    @overload
    async def find(self, criteria: LogicalOperator = "and", **kwargs) -> IdentityVerificationEntity | None: ...

    async def find(self, *args, **kwargs):
        raise NotImplementedError

