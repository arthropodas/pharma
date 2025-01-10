from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from api.utils.error_messages import error_code_402, error_code_403, error_code_404
import jwt
from decouple import config
from datetime import datetime, timezone
from user_management.models import UserData
from django.http import JsonResponse


class CustomIsAuthenticated(BaseAuthentication):
    def authenticate(self, request):
        
        token = request.META.get("HTTP_AUTHORIZATION")
        if not token or not token.startswith("Bearer "):
            raise AuthenticationFailed(error_code_403())

        token = token.split(" ")[1]
        print("token", token, token)

        try:
            decoded_token = jwt.decode(
                token, config("SECRET_KEY"), algorithms=["HS256"]
            )
            if decoded_token["token_type"] != "access":
                raise AuthenticationFailed(error_code_402())

            if "exp" in decoded_token:
                expiry_timestamp = datetime.fromtimestamp(
                    decoded_token["exp"], tz=timezone.utc
                )
                if expiry_timestamp < datetime.now(tz=timezone.utc):
                    raise AuthenticationFailed(error_code_404())
            else:
                raise AuthenticationFailed(error_code_402())
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed(error_code_404())
        except jwt.InvalidTokenError:
            raise AuthenticationFailed(error_code_402())
        return self.get_user_and_token(request, token)
    def get_user_and_token(self, request, token):
        
        decoded_token = jwt.decode(token, config("SECRET_KEY"), algorithms=["HS256"])
        user_id = decoded_token.get("user_id")
        try:
            user = UserData.objects.get(id=user_id)
        except UserData.DoesNotExist:
            raise AuthenticationFailed(error_code_403())
        return user, token

    def authenticate_header(self, request):
        return 'Bearer realm="api"'

