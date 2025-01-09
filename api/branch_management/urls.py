from django.urls import path
from .views import BranchView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("manage/", BranchView.as_view(), name="branch_view"),
    
]
