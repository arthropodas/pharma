from django.urls import path
from .views import UserRegistrationView, GoogleLoginView, UserLoginAPIView, AddStaffView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="user_registration"),
    path("google_login/", GoogleLoginView.as_view(), name="google_login"),
    path("login/", UserLoginAPIView.as_view(), name="token_obtain_pair"),
    path("refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("staff/add/", AddStaffView.as_view(), name="staff_add"),
]
