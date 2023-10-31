import requests
from ..compat import Iterable
from ..objects import OperationStatusObject
from .api_request import APIRequest
from _typeshed import Incomplete
from typing import Optional

class GetOperationStatusRequest(APIRequest):
    method: str
    url: Incomplete
    def __init__(self, session: requests.Session, operation_id: str, fields: Optional[Iterable[str]] = ..., **kwargs) -> None: ...
    def process_args(self, fields: Optional[Iterable[str]]) -> None: ...
    def process_json(self, js: Optional[dict]) -> OperationStatusObject: ...
