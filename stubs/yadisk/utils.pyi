from .exceptions import *
import requests.exceptions
from .compat import Callable
from typing import Optional, TypeVar, Union

def get_exception(response: requests.Response) -> YaDiskError: ...
T = TypeVar('T')

def auto_retry(func: Callable[[], T], n_retries: Optional[int] = ..., retry_interval: Optional[Union[int, float]] = ...) -> T: ...
