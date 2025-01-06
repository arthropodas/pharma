from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .models import UserData
from decouple import config
from google.oauth2 import id_token
from google.auth.exceptions import GoogleAuthError
import jwt
import uuid
from django.conf import settings    
from datetime import datetime, timedelta, timezone
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from google.auth.transport import requests
from .validators import validate_dob, validate_email, validate_first_name, validate_phone_number, validatea_last_name, validate_password
from api.utils.error_messages import error_code_e401,error_code_e402
class UserRegistrationView(APIView):
    def post(self, request):
        try:
            
            email = request.data.get('email')
            password = request.data.get('password')
            first_name = request.data.get('firstName')
            last_name = request.data.get('lastName')
            phone_number = request.data.get('phoneNumber')
            dob = request.data.get('dob')
           
            
            validate_first_name(first_name)
            validatea_last_name(last_name)
            validate_dob(dob)
            validate_email(email,True)
            validate_password(password)
            validate_phone_number(phone_number)
  
                     
            user = UserData.objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                dob=dob,
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

class UserLoginAPIView(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            # Validate email and password
            validate_email(email, register=False)
            validate_password(password)

            # Authenticate the user using email and password
            user = authenticate(request, email=email, password=password)

            if user is None:
                return Response(error_code_e401(), status=status.HTTP_401_UNAUTHORIZED)

            # Generate JWT tokens for the authenticated user
            from rest_framework_simplejwt.tokens import RefreshToken
            refresh = RefreshToken.for_user(user)

            data = {
                'accessToken': str(refresh.access_token),
                'refreshToken': str(refresh),
                'userType': user.user_type
            }

            return Response(data, status=status.HTTP_200_OK)

        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
           
class GoogleLoginView(APIView):
    def post(self, request):
        try:
            # Get the token from the request
            token = request.data.get("token")
            print("token: ", token)

            if not token:
                return Response(
                    {"error": "Token is required."}, status=status.HTTP_400_BAD_REQUEST
                )

            
            client_id = config("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY")
            payload = id_token.verify_oauth2_token(token, requests.Request(), client_id)
            print("payload: .......", payload)
            email = payload.get("email")
            user = UserData.objects.filter(email=email)
            if(user == None):
                user = UserData.objects.create_user(
                email=email,
                first_name=given_name,
            )
            name =  payload.get("name")
            given_name = payload.get("given_name")
            picture = payload.get("picture")
        
            
            
            
            current_time = datetime.now(timezone.utc)
            access_expiration_time = current_time + timedelta(
                days=int(config("ACCESS_TOKEN_LIFETIME"))
            )
            refresh_expiration_time = current_time + timedelta(
                days=int(config("REFRESH_TOKEN_LIFETIME"))
            )

            access_payload = {
                "token_type": "access",
                "exp": int(
                    access_expiration_time.timestamp()
                ),  # Expiration time in seconds since epoch
                "iat": int(
                    current_time.timestamp()
                ),  
                "jti": str(uuid.uuid4()), 
                "user_id": user.id, 
            }

            refresh_payload = {
                "token_type": "refresh",
                "exp": int(refresh_expiration_time.timestamp()),
                "iat": int(current_time.timestamp()),
                "jti": str(uuid.uuid4()),
                "user_id": user.id,
            }

            access_token = jwt.encode(
                access_payload, settings.SECRET_KEY, algorithm="HS256"
            )
            refresh_token = jwt.encode(
                refresh_payload, settings.SECRET_KEY, algorithm="HS256"
            )

            print("Access Token: ", access_token)
            print("Refresh Token: ", refresh_token)

            return Response(
                {
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "name": name,
                    "givenName": given_name,
                    "profile": picture,
                },
                status=status.HTTP_200_OK,
            )

        except ValueError as e:
            print("Token verification error: ", str(e))
            return Response(error_code_e402(), status=status.HTTP_401_UNAUTHORIZED)

        except GoogleAuthError as e:

            return Response(error_code_e402(), status=status.HTTP_401_UNAUTHORIZED)


        except Exception as e:
            print(f"Error: {e}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    