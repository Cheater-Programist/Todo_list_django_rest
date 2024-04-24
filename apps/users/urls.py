from django.urls import path 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import UserAPI

urlpatterns = [
    path('', UserAPI.as_view(), name="api_users"),
    path('login/', TokenObtainPairView.as_view(), name='api_users_login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='api_users_refresh'),
]