from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import LogInView, SignUpView, LogOutRenderView

app_name = 'accounts'

urlpatterns = [
    path('log-in/', LogInView.as_view(), name='log_in'),
    path("log-out/", LogOutRenderView.as_view(), name="logout-confirmation"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
]