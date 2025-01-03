from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .models import UserData
from django.contrib.auth.hashers import make_password
from .validators import validate_dob, validate_email, validate_first_name, validate_phone_number, validate_user_type, validatea_last_name
class UserRegistrationView(APIView):
    def post(self, request):
        try:
            
            email = request.data.get('email')
            password = request.data.get('password')
            first_name = request.data.get('firstName')
            last_name = request.data.get('lastName')
            phone_number = request.data.get('phoneNumber')
            dob = request.data.get('dob')
            user_type = request.data.get('userType')
            
            validate_first_name(first_name)
            validatea_last_name(last_name)
            validate_dob(dob)
            validate_email(email)
            validate_phone_number(phone_number)
            validate_user_type(user_type)   
                     
            import pdb;pdb.set_trace()        
            user = UserData.objects.create_user(
                email=email,
                password=make_password(password),
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                dob=dob,
                user_type=user_type,
            )
            return Response(
                {"message": "User created successfully", "user_id": user.id},
                status=status.HTTP_200_OK,
            )

        except ValidationError as e:
            # Handle validation errors
            

            return Response(
                e.detail,
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            print("error creating user", e)
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
