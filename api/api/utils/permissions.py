from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.response import Response
from user_management.models import UserData
from branch_management.models import Branch
from rest_framework.exceptions import ValidationError
import jwt
from decouple import config
from api.utils.error_messages import (
    error_code_403,
    error_code_404,
    error_code_405,
    error_code_2003,
)


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_type != 3:
            raise PermissionDenied(error_code_405())  # User is not a staff member

        return True


class IsOwner(BasePermission):
    def has_permission(self, request, view):

        branch_id = view.kwargs["pk"]
        try:

            branch = Branch.objects.get(id=branch_id)

            if branch.owner.id != request.user.id:
                raise PermissionDenied(error_code_405())
            return True
        except Branch.DoesNotExist:
            return Response(error_code_2003(), status=status.HTTP_400_BAD_REQUEST)
