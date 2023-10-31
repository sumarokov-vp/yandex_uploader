from ..yadisk import YaDisk
from .yadisk_object import YaDiskObject
from typing import NoReturn, Optional

class DiskInfoObject(YaDiskObject):
    max_file_size: Optional[int]
    paid_max_file_size: Optional[int]
    unlimited_autoupload_enabled: Optional[bool]
    total_space: Optional[int]
    trash_size: Optional[int]
    is_paid: Optional[bool]
    used_space: Optional[int]
    system_folders: SystemFoldersObject
    user: UserObject
    revision: Optional[int]
    def __init__(self, disk_info: Optional[dict] = ..., yadisk: Optional['YaDisk'] = ...) -> None: ...

class SystemFoldersObject(YaDiskObject):
    odnoklassniki: Optional[str]
    google: Optional[str]
    instagram: Optional[str]
    vkontakte: Optional[str]
    attach: Optional[str]
    mailru: Optional[str]
    downloads: Optional[str]
    applications: Optional[str]
    facebook: Optional[str]
    social: Optional[str]
    messenger: Optional[str]
    calendar: Optional[str]
    photostream: Optional[str]
    screenshots: Optional[str]
    scans: Optional[str]
    def __init__(self, system_folders: Optional[dict] = ..., yadisk: Optional['YaDisk'] = ...) -> None: ...

class UserObject(YaDiskObject):
    country: Optional[str]
    login: Optional[str]
    display_name: Optional[str]
    uid: Optional[str]
    def __init__(self, user: Optional[dict] = ..., yadisk: Optional['YaDisk'] = ...) -> None: ...

class UserPublicInfoObject(UserObject):
    country: NoReturn
    def __init__(self, public_user_info: Optional[dict] = ..., yadisk: Optional['YaDisk'] = ...) -> None: ...
