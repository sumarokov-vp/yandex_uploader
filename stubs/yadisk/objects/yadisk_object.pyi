from ..yadisk import YaDisk
from typing import Any, Callable, Iterator, Optional

class YaDiskObject:
    FIELD_TYPES: dict
    FIELDS: dict
    ALIASES: dict
    def __init__(self, field_types: Optional[dict] = ..., yadisk: Optional['YaDisk'] = ...) -> None: ...
    def set_field_types(self, field_types: dict) -> None: ...
    def set_field_type(self, field: str, type: Callable) -> None: ...
    def set_alias(self, alias: str, name: str) -> None: ...
    def remove_alias(self, alias: str) -> None: ...
    def remove_field(self, field: str) -> None: ...
    def import_fields(self, source_dict: Optional[dict]) -> None: ...
    def __setattr__(self, attr: str, value: Any) -> None: ...
    def __getattr__(self, attr: str) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __iter__(self) -> Iterator[dict]: ...
    def __len__(self) -> int: ...
