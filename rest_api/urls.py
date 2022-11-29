from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('token', views.LoginAPIView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('register', views.RegisterView.as_view(), name='auth_register'),
    path('add_credit', views.AddCreditView.as_view(), name='add_credit'),
    path('health', views.health, name='health')
]
