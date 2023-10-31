from ..yadisk import YaDisk
from .yadisk_object import YaDiskObject
from typing import Optional

class TokenObject(YaDiskObject):
    access_token: Optional[str]
    refresh_token: Optional[str]
    token_type: Optional[str]
    expires_in: Optional[int]
    def __init__(self, token: Optional[dict] = ..., yadisk: Optional['YaDisk'] = ...) -> None: ...

class TokenRevokeStatusObject(YaDiskObject):
    status: Optional[str]
    def __init__(self, token_revoke_status: Optional[dict] = ..., yadisk: Optional['YaDisk'] = ...) -> None: ...
