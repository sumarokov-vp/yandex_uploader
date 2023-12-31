from ._internal_utils import to_native_string as to_native_string
from .compat import Morsel as Morsel, MutableMapping as MutableMapping, cookielib as cookielib, urlparse as urlparse, urlunparse as urlunparse
from _typeshed import Incomplete
from collections.abc import Generator

class MockRequest:
    type: Incomplete
    def __init__(self, request) -> None: ...
    def get_type(self): ...
    def get_host(self): ...
    def get_origin_req_host(self): ...
    def get_full_url(self): ...
    def is_unverifiable(self): ...
    def has_header(self, name): ...
    def get_header(self, name, default: Incomplete | None = ...): ...
    def add_header(self, key, val) -> None: ...
    def add_unredirected_header(self, name, value) -> None: ...
    def get_new_headers(self): ...
    @property
    def unverifiable(self): ...
    @property
    def origin_req_host(self): ...
    @property
    def host(self): ...

class MockResponse:
    def __init__(self, headers) -> None: ...
    def info(self): ...
    def getheaders(self, name) -> None: ...

def extract_cookies_to_jar(jar, request, response) -> None: ...
def get_cookie_header(jar, request): ...
def remove_cookie_by_name(cookiejar, name, domain: Incomplete | None = ..., path: Incomplete | None = ...) -> None: ...

class CookieConflictError(RuntimeError): ...

class RequestsCookieJar(cookielib.CookieJar, MutableMapping):
    def get(self, name, default: Incomplete | None = ..., domain: Incomplete | None = ..., path: Incomplete | None = ...): ...
    def set(self, name, value, **kwargs): ...
    def iterkeys(self) -> Generator[Incomplete, None, None]: ...
    def keys(self): ...
    def itervalues(self) -> Generator[Incomplete, None, None]: ...
    def values(self): ...
    def iteritems(self) -> Generator[Incomplete, None, None]: ...
    def items(self): ...
    def list_domains(self): ...
    def list_paths(self): ...
    def multiple_domains(self): ...
    def get_dict(self, domain: Incomplete | None = ..., path: Incomplete | None = ...): ...
    def __contains__(self, name) -> bool: ...
    def __getitem__(self, name): ...
    def __setitem__(self, name, value) -> None: ...
    def __delitem__(self, name) -> None: ...
    def set_cookie(self, cookie, *args, **kwargs): ...
    def update(self, other) -> None: ...
    def copy(self): ...
    def get_policy(self): ...

def create_cookie(name, value, **kwargs): ...
def morsel_to_cookie(morsel): ...
def cookiejar_from_dict(cookie_dict, cookiejar: Incomplete | None = ..., overwrite: bool = ...): ...
def merge_cookies(cookiejar, cookies): ...
