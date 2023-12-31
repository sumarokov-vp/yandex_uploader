from . import sessions as sessions
from _typeshed import Incomplete

def request(method, url, **kwargs): ...
def get(url, params: Incomplete | None = ..., **kwargs): ...
def options(url, **kwargs): ...
def head(url, **kwargs): ...
def post(url, data: Incomplete | None = ..., json: Incomplete | None = ..., **kwargs): ...
def put(url, data: Incomplete | None = ..., **kwargs): ...
def patch(url, data: Incomplete | None = ..., **kwargs): ...
def delete(url, **kwargs): ...
