from rest_framework.exceptions import ValidationError
import re
from api.utils.error_messages import (
    error_code_1015,
    error_code_1016,
    error_code_1017,
    error_code_2001,
    error_code_2002,
)
from .models import Branch
from user_management.models import UserData
error_messages = {
    "branch_name": error_code_2001,
    "owner_id": error_code_1015,
}


def validate_required(value, field_name):
    if not value:
        raise ValidationError(error_messages[field_name]())


def validate_branch_name(branch_name):
    validate_required(branch_name, "branch_name")
    branch_name= re.sub(r'\s+', ' ', branch_name.strip())
    if (
        
        len(branch_name) < 2
        or len(branch_name) > 100
    ):
        raise ValidationError(error_code_2002())


def validate_owner_id(owner_id):
    validate_required(owner_id, "owner_id")
    try:
        owner = UserData.objects.filter(status=1, id=owner_id).first()
        if not owner:
            raise ValidationError(error_code_1017())
        return owner
    except ValueError as e:
        print("e...........",e)
        raise ValidationError(error_code_1016())
