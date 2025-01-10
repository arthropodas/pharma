from django.urls import path
from .views import BranchView, BranchGetView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("branch/", BranchView.as_view(), name="branch_view"),   
    path("branch/<int:pk>/", BranchGetView.as_view(), name="get_branch"),
]
