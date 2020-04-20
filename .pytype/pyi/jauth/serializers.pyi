# (generated with --quick)

import datetime
import jauth.models
import requests.models
from typing import Any, Dict, Type, TypeVar

AccountKitAccessToken: Type[jauth.models.AccountKitAccessToken]
AccountKitUser: Type[jauth.models.AccountKitUser]
FacebookAccessToken: Type[jauth.models.FacebookAccessToken]
FacebookUser: Type[jauth.models.FacebookUser]
GoogleAccessToken: Type[jauth.models.GoogleAccessToken]
GoogleUser: Type[jauth.models.GoogleUser]
Token: Any
User: Any
_: Any
now: Any
serializers: module
timedelta: Type[datetime.timedelta]
transaction: module

_T0 = TypeVar('_T0')

class AccountKitAuthTokenSerializer(Any):
    access_token: Any
    code: Any
    def validate(self, attrs: _T0) -> _T0: ...

class AuthResultSerializer(Any):
    def to_representation(self, instance) -> Dict[str, Any]: ...

class FacebookAuthTokenSerializer(Any):
    access_token: Any
    code: Any
    def validate(self, attrs: _T0) -> _T0: ...

class GoogleAuthTokenSerializer(Any):
    access_token: Any
    code: Any
    def validate(self, attrs: _T0) -> _T0: ...

def account_kit_get_access_token(code: str) -> requests.models.Response: ...
def account_kit_me(access_token: str) -> requests.models.Response: ...
def facebook_get_access_token(code: str) -> requests.models.Response: ...
def facebook_me(access_token: str) -> requests.models.Response: ...
def google_get_access_token(code: str) -> requests.models.Response: ...
def google_me(access_token: str) -> requests.models.Response: ...
