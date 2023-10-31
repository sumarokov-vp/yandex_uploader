import requests
from ..compat import Set
from _typeshed import Incomplete
from typing import Optional, TypeVar, Union

class APIRequest:
    url: Optional[str]
    method: Optional[str]
    content_type: str
    timeout: Incomplete
    n_retries: Optional[int]
    success_codes: Set[int]
    retry_interval: Optional[Union[int, float]]
    request: Optional[requests.PreparedRequest]
    response: Optional[requests.Response]
    T = TypeVar('T')
    session: Incomplete
    args: Incomplete
    send_kwargs: Incomplete
    headers: Incomplete
    data: Incomplete
    params: Incomplete
    def __init__(self, session: requests.Session, args: dict, **kwargs) -> None: ...
    def process_args(self) -> None: ...
    def prepare(self) -> None: ...
    def send(self) -> requests.Response: ...
    def process_json(self, js: Optional[dict], **kwargs) -> T: ...
    def process(self, **kwargs) -> T: ...
