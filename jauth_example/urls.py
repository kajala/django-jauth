from django.conf.urls import url
from jauth.views import AccountKitRedirectView, FacebookRedirectView, FacebookDeauthorizeView, FacebookDeleteView, \
    GoogleRedirectView
from jauth_example.views import HomeView, LoginView, LogoutView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='jauth-example-home'),
    url(r'^accounts/login', LoginView.as_view(), name='jauth-example-login'),
    url(r'^accounts/logout', LogoutView.as_view(), name='jauth-example-logout'),
    url(r'^accounts/account-kit-redirect', AccountKitRedirectView.as_view(), name='jauth-example-account-kit-redirect'),
    url(r'^accounts/facebook-redirect', FacebookRedirectView.as_view(), name='jauth-example-facebook-redirect'),
    url(r'^accounts/facebook-deauthorize', FacebookDeauthorizeView.as_view(), name='jauth-example-facebook-deauthorize'),
    url(r'^accounts/facebook-delete', FacebookDeleteView.as_view(), name='jauth-example-facebook-delete'),
    url(r'^accounts/google-redirect', GoogleRedirectView.as_view(), name='jauth-example-google-redirect'),
]
