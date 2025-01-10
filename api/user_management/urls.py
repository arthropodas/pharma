from django.urls import path
from .views import UserRegistrationView, GoogleLoginView, UserLoginAPIView, AddStaffView,UserManagementView,ForgotPasswordView, ResetPasswordAPIView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("user/register/", UserRegistrationView.as_view(), name="user_registration"),
    path("user/google_login/", GoogleLoginView.as_view(), name="google_login"),
    path('user/login/', UserLoginAPIView.as_view(), name="login_user"),
    path("user/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("user/staff/<int:pk>/", AddStaffView.as_view(), name="staff_management"),
    path(
        "user/",UserManagementView.as_view(), name='user_management'),
    path("user/forgot-password/",ForgotPasswordView.as_view(), name="forgot_password"),
    path('user/reset-password', ResetPasswordAPIView.as_view(), name='reset_password'),

]
