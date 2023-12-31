import time
from ._internal_utils import to_native_string as to_native_string
from .adapters import HTTPAdapter as HTTPAdapter
from .compat import Mapping as Mapping, cookielib as cookielib, urljoin as urljoin, urlparse as urlparse
from .cookies import RequestsCookieJar as RequestsCookieJar, cookiejar_from_dict as cookiejar_from_dict, extract_cookies_to_jar as extract_cookies_to_jar, merge_cookies as merge_cookies
from .exceptions import ChunkedEncodingError as ChunkedEncodingError, ContentDecodingError as ContentDecodingError, InvalidSchema as InvalidSchema, TooManyRedirects as TooManyRedirects
from .hooks import default_hooks as default_hooks, dispatch_hook as dispatch_hook
from .models import DEFAULT_REDIRECT_LIMIT as DEFAULT_REDIRECT_LIMIT, PreparedRequest as PreparedRequest, REDIRECT_STATI as REDIRECT_STATI, Request as Request
from .status_codes import codes as codes
from .structures import CaseInsensitiveDict as CaseInsensitiveDict
from .utils import DEFAULT_PORTS as DEFAULT_PORTS, default_headers as default_headers, get_auth_from_url as get_auth_from_url, get_environ_proxies as get_environ_proxies, get_netrc_auth as get_netrc_auth, requote_uri as requote_uri, resolve_proxies as resolve_proxies, rewind_body as rewind_body, should_bypass_proxies as should_bypass_proxies, to_key_val_list as to_key_val_list
from _typeshed import Incomplete
from collections.abc import Generator

preferred_clock = time.time

def merge_setting(request_setting, session_setting, dict_class=...): ...
def merge_hooks(request_hooks, session_hooks, dict_class=...): ...

class SessionRedirectMixin:
    def get_redirect_target(self, resp): ...
    def should_strip_auth(self, old_url, new_url): ...
    def resolve_redirects(self, resp, req, stream: bool = ..., timeout: Incomplete | None = ..., verify: bool = ..., cert: Incomplete | None = ..., proxies: Incomplete | None = ..., yield_requests: bool = ..., **adapter_kwargs) -> Generator[Incomplete, None, None]: ...
    def rebuild_auth(self, prepared_request, response) -> None: ...
    def rebuild_proxies(self, prepared_request, proxies): ...
    def rebuild_method(self, prepared_request, response) -> None: ...

class Session(SessionRedirectMixin):
    __attrs__: Incomplete
    headers: Incomplete
    auth: Incomplete
    proxies: Incomplete
    hooks: Incomplete
    params: Incomplete
    stream: bool
    verify: bool
    cert: Incomplete
    max_redirects: Incomplete
    trust_env: bool
    cookies: Incomplete
    adapters: Incomplete
    def __init__(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def prepare_request(self, request): ...
    def request(self, method, url, params: Incomplete | None = ..., data: Incomplete | None = ..., headers: Incomplete | None = ..., cookies: Incomplete | None = ..., files: Incomplete | None = ..., auth: Incomplete | None = ..., timeout: Incomplete | None = ..., allow_redirects: bool = ..., proxies: Incomplete | None = ..., hooks: Incomplete | None = ..., stream: Incomplete | None = ..., verify: Incomplete | None = ..., cert: Incomplete | None = ..., json: Incomplete | None = ...): ...
    def get(self, url, **kwargs): ...
    def options(self, url, **kwargs): ...
    def head(self, url, **kwargs): ...
    def post(self, url, data: Incomplete | None = ..., json: Incomplete | None = ..., **kwargs): ...
    def put(self, url, data: Incomplete | None = ..., **kwargs): ...
    def patch(self, url, data: Incomplete | None = ..., **kwargs): ...
    def delete(self, url, **kwargs): ...
    def send(self, request, **kwargs): ...
    def merge_environment_settings(self, url, proxies, stream, verify, cert): ...
    def get_adapter(self, url): ...
    def close(self) -> None: ...
    def mount(self, prefix, adapter) -> None: ...

def session(): ...
