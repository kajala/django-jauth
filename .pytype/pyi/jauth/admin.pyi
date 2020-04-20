# (generated with --quick)

import jauth.models
from typing import Any, List, Tuple, Type

AccountKitAccessToken: Type[jauth.models.AccountKitAccessToken]
AccountKitUser: Type[jauth.models.AccountKitUser]
FacebookAccessToken: Type[jauth.models.FacebookAccessToken]
FacebookUser: Type[jauth.models.FacebookUser]
GoogleAccessToken: Type[jauth.models.GoogleAccessToken]
GoogleUser: Type[jauth.models.GoogleUser]
admin: module
p: str
required_params: List[str]
settings: Any

class AccountKitAdmin(JauthAdminBase):
    exclude: Tuple[nothing, ...]

class FacebookAdmin(JauthAdminBase):
    exclude: Tuple[nothing, ...]

class GoogleAdmin(JauthAdminBase):
    exclude: Tuple[nothing, ...]

class JauthAdminBase(Any): ...
