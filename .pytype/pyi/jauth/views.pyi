# (generated with --quick)

import jauth.models
import jauth.serializers
from typing import Any, Callable, Dict, Mapping, Sequence, Tuple, Type, TypeVar, Union

APIView: Any
AccountKitAuthTokenSerializer: Type[jauth.serializers.AccountKitAuthTokenSerializer]
AuthResultSerializer: Type[jauth.serializers.AuthResultSerializer]
FacebookAccessToken: Type[jauth.models.FacebookAccessToken]
FacebookAuthTokenSerializer: Type[jauth.serializers.FacebookAuthTokenSerializer]
FacebookUser: Type[jauth.models.FacebookUser]
GoogleAuthTokenSerializer: Type[jauth.serializers.GoogleAuthTokenSerializer]
HttpRequest: Any
HttpResponse: Any
Request: Any
TemplateView: Any
auth: module
json: module
logger: logging.Logger
logging: module
redirect: Any
settings: Any

AnyStr = TypeVar('AnyStr', str, bytes)

class AccountKitRedirectView(OAuthRedirectViewBase):
    serializer_class: Type[jauth.serializers.AccountKitAuthTokenSerializer]

class FacebookDeauthorizeView(Any):
    def post(self, request, *args, **kwargs) -> dict: ...

class FacebookDeleteView(Any):
    def post(self, request, *args, **kwargs) -> dict: ...

class FacebookRedirectView(OAuthRedirectViewBase):
    serializer_class: Type[jauth.serializers.FacebookAuthTokenSerializer]

class GoogleRedirectView(OAuthRedirectViewBase):
    serializer_class: Type[jauth.serializers.GoogleAuthTokenSerializer]

class OAuthRedirectViewBase(Any):
    result_serializer_class: Type[jauth.serializers.AuthResultSerializer]
    serializer_class: None
    template_name: str
    def get(self, request, *args, **kwargs) -> Any: ...
    def get_context_data(self, **kw) -> Dict[str, Any]: ...
    def post(self, request, *args, **kwargs) -> Any: ...

def facebook_parse_signed_request(signed_request: str) -> dict: ...
def urlencode(query: Union[Mapping, Sequence[Tuple[Any, Any]]], doseq: bool = ..., safe: AnyStr = ..., encoding: str = ..., errors: str = ..., quote_via: Callable[[str, AnyStr, str, str], str] = ...) -> str: ...
