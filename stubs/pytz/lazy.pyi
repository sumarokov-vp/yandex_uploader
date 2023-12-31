from _typeshed import Incomplete
from collections import Mapping as DictMixin

class LazyDict(DictMixin):
    data: Incomplete
    def __getitem__(self, key): ...
    def __contains__(self, key) -> bool: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def keys(self): ...

class LazyList(list):
    def __new__(cls, fill_iter: Incomplete | None = ...): ...

class LazySet(set):
    def __new__(cls, fill_iter: Incomplete | None = ...): ...
