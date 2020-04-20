# (generated with --quick)

from typing import Any

JSONField: Any
User: Any
_: Any
models: module
now: Any
settings: Any

class AccountKitAccessToken(OAuthAccessToken):
    ext_user: Any

class AccountKitUser(OAuthUser):
    phone: str

class FacebookAccessToken(OAuthAccessToken):
    ext_user: Any

class FacebookUser(OAuthUser):
    email: str
    first_name: str
    last_name: str
    name: str
    phone: str
    picture_url: str

class GoogleAccessToken(OAuthAccessToken):
    ext_user: Any

class GoogleUser(OAuthUser):
    email: str
    first_name: str
    last_name: str
    locale: str
    name: str
    picture_url: str
    verified_email: bool

class OAuthAccessToken(Any):
    Meta: type
    access_token: Any
    expire_time: Any

class OAuthUser(Any):
    Meta: type
    created: Any
    ext_user_id: Any
    me: Any
    user: Any
