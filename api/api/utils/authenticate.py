from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from user_management.models import UserData  # Import your custom user model

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = UserData.objects.get(email=email)
            if check_password(password, user.password):
                return user
        except UserData.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserData.objects.get(pk=user_id)
        except UserData.DoesNotExist:
            return None