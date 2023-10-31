import requests
from ..compat import Iterable
from ..objects import DiskInfoObject
from .api_request import APIRequest
from typing import Optional

class DiskInfoRequest(APIRequest):
    url: str
    method: str
    def __init__(self, session: requests.Session, fields: Optional[Iterable[str]] = ..., **kwargs) -> None: ...
    def process_args(self, fields: Optional[Iterable[str]]) -> None: ...
    def process_json(self, js: Optional[dict]) -> DiskInfoObject: ...
