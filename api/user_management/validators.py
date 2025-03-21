from rest_framework.exceptions import ValidationError
from api.utils.error_messages import (
    error_code_1001,
    error_code_1002,
    error_code_1003,
    error_code_1004,
    error_code_1005,
    error_code_1006,
    error_code_1007,
    error_code_1008,
    error_code_1009,
    error_code_1010,
    error_code_1011,
    error_code_1012,
    error_code_1013,
    error_code_1014,
    error_code_1018,
    error_code_1019,
    error_code_1020,
    error_code_1021,
)
import re
import datetime
from .models import UserData

error_messages = {
    "first_name": error_code_1001,
    "email": error_code_1003,
    "user_type": error_code_1005,
    "password": error_code_1011,
}


def validate_required(value, field_name):
    if not value:
        raise ValidationError(error_messages[field_name]())


def validate_first_name(name):
    print("name", name)
    validate_required(name, "first_name")
    name_regex = r"^(?! )[A-Za-z]+(?: [A-Za-z]+)*(?<! )$"
    name = re.sub(r"\s+", " ", name.strip())
    if (not re.match(name_regex, name)) or len(name) < 2 or len(name) > 100:
        raise ValidationError(error_code_1002())


def validate_email(email, register):
    validate_required(email, "email")
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if not re.match(email_regex, email):
        raise ValidationError(error_code_1004())
    email = UserData.objects.filter(email=email).first()
    if register:
        if email:
            raise ValidationError(error_code_1010())


def validate_gender(gender):
    if gender:
        try:
            gender = int(gender)
            allowed_types = {1, 2, 3}
            if gender not in allowed_types:
                raise ValidationError(error_code_1006())
        except ValueError:
            raise ValidationError(error_code_1006())


def validate_phone_number(phone_number):
    if phone_number:
        phone_regex = r"^\+?\d{1,15}$"
        if not re.match(phone_regex, phone_number):
            raise ValidationError(error_code_1007())


def validate_last_name(last_name):
    if last_name:
        if len(last_name.strip()) < 2 or len(last_name.strip()) > 100:
            raise ValidationError(error_code_1008())


def validate_dob(dob):
    if dob:
        pattern = r"^(20[0-9]{2})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
        if not re.match(pattern, dob):
            raise ValidationError(error_code_1009())


def validate_password(password):
    # Error codes mapping based on field name
    error_codes = {
        "password": {
            "required": error_code_1011,
            "invalid": error_code_1012,
        },
        "currentPassword": {
            "required": error_code_1018,
            "invalid": error_code_1019,
        },
        "newPassword": {
            "required": error_code_1020,
            "invalid": error_code_1021,
        },
    }

    if not password:
        # Raise error if password is not provided
        raise ValidationError(error_codes[field_name]["required"]())

    PASSWORD_REGEX = (
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%?&])[A-Za-z\d@$!%?&]{8,}$"
    )

    # Check if password matches the regex
    if not re.match(PASSWORD_REGEX, password):
        raise ValidationError(error_codes[field_name]["invalid"]())


def validate_profile_image(profile_image):
    if profile_image:
        allowed_content_types = ["jpeg", "jpg", "png"]

        if (
            profile_image.content_type.split("/")[1].lower()
            not in allowed_content_types
        ):
            raise ValidationError(error_code_1013())

        max_file_size = 2 * 1024 * 1024

        if profile_image.size > max_file_size:
            raise ValidationError(error_code_1014())

    return None


def validate_email_edit(email, user_id):
    user = UserData.objects.filter(email=email).exclude(id=user_id).exists()
    if user:
        raise ValidationError(error_code_1010())
