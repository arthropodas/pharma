from rest_framework.exceptions import ValidationError
from api.utils.error_messages import error_code_1001,error_code_1002,error_code_1003,error_code_1004,error_code_1005, error_code_1006, error_code_1007, error_code_1008, error_code_1009, error_code_1010
import re
import datetime
from .models import UserData

error_messages = {
    "frist_name": error_code_1001,
    "email": error_code_1003,
    "user_type": error_code_1005,
  
}

def validate_required(value, field_name):
    if not value:
        raise ValidationError(error_messages[field_name]())
def validate_first_name(name):
    validate_required(name,"first_name")
    
    if not name or len(name.strip()) < 2 or len(name.strip()) > 100:
        raise ValidationError(error_code_1002())

def validate_email(email):
    validate_required(email,"email")
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        raise ValidationError(error_code_1004())
    email = UserData.objects.filter(email=email).first()
    if email:
        raise ValidationError(error_code_1010())
    
def validate_user_type(user_type):
    if not user_type:
        raise ValidationError(error_code_1005())
    allowed_types = {1, 2, 3}  # ADMIN, OWNER, STAFF
    if user_type not in allowed_types:
        raise ValidationError(error_code_1006())    

def validate_phone_number(phone_number):
    if phone_number:
        phone_regex = r'^\+?\d{1,15}$'
        if not re.match(phone_regex, phone_number):
            raise ValidationError(error_code_1007())
def validatea_last_name(last_name):
    if last_name:
        if len(last_name.strip()) < 2 or len(last_name.strip()) > 100:
            raise ValidationError(error_code_1008())
def validate_dob(dob):
    if dob:
        try:
            date_object = datetime(dob, '%Y-%m-%d')
        except ValueError:
            raise ValidationError(error_code_1009())