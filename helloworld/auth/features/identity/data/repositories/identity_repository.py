from __future__ import annotations

from abc import ABC
from typing import overload

from helloworld.core.data import AbstractRepository, TModel
from helloworld.core.data.repositories.abstract_repository import LogicalOperator
from helloworld.auth.features.identity import IdentityEntity

class IdentityRepository(AbstractRepository[IdentityEntity, TModel], ABC):
    @overload
    async def find(self, id: int) -> IdentityEntity | None: ...

    @overload
    async def find(self, username: str) -> IdentityEntity | None: ...

    @overload
    async def find(self, email: str) -> IdentityEntity | None: ...

    @overload
    async def find(self, phone: str) -> IdentityEntity | None: ...

    @overload
    async def find(self, criteria: LogicalOperator = "and", **kwargs) -> IdentityEntity | None: ...

    async def find(self, *args, **kwargs):
        raise NotImplementedError