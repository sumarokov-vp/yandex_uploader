from ..yadisk import YaDisk
from .yadisk_object import YaDiskObject
from typing import Optional

class OperationStatusObject(YaDiskObject):
    def __init__(self, operation_status: Optional[dict] = ..., yadisk: Optional['YaDisk'] = ...) -> None: ...
