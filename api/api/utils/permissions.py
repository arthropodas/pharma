from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from user_management.models import UserData
import jwt
from decouple import config
from api.utils.error_messages import error_code_e403

class IsStaff(BasePermission):
    def has_permission(self, request, view):
        token = request.META.get("HTTP_AUTHORIZATION")
        
        if not token:
            raise PermissionDenied(error_code_e403())  # Unauthorized if no token is provided
        import pdb;pdb.set_trace()
        try:
            token = token.split(" ")[1]  # Extract token from 'Bearer <token>'
            decoded_token = jwt.decode(token, config("SECRET_KEY"), algorithms=["HS256"])
            user_id = decoded_token.get("user_id")

            if not user_id:
                raise PermissionDenied(error_code_e403())  # Token doesn't have user_id

            user = UserData.objects.get(id=user_id)

            # Check if the user is a staff member (user_type == 3)
            if user.user_type != 3:
                raise PermissionDenied(error_code_e403())  # User is not a staff member

            return True
        except jwt.ExpiredSignatureError:
            raise PermissionDenied(error_code_e403())  # Token has expired
        except jwt.InvalidTokenError:
            raise PermissionDenied(error_code_e403())  # Invalid token
        except UserData.DoesNotExist:
            raise PermissionDenied(error_code_e403())  # User not found
