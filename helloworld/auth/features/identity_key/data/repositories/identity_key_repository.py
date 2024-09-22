from __future__ import annotations

from abc import ABC

from helloworld.core.data import AbstractRepository, TModel
from helloworld.auth.features.identity_key import IdentityKeyEntity

class IdentityKeyRepository(AbstractRepository[IdentityKeyEntity, TModel], ABC): ...