from django.urls import path
from apps.login.views import CustomTokenObtainPairView, RegisterView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path(
        "token/",
        CustomTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterView.as_view(), name="auth_register"),
]
