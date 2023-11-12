from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import registration, index
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('reg/', views.registration, name="registeration"),
    path('auth/', views.auth, name="auth"),
]


