from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserData
from decouple import config
from google.oauth2 import id_token
from google.auth.exceptions import GoogleAuthError
import jwt
import uuid
from django.conf import settings
from datetime import datetime, timedelta, timezone
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from google.auth.transport import requests
from api.utils.permissions import IsStaff, IsOwner
from branch_management.models import Branch
from django.core.mail import send_mail
from api.utils.functions import generate_reset_token, send_email
from django.core.cache import cache

from .validators import (
    validate_dob,
    validate_email,
    validate_first_name,
    validate_phone_number,
    validate_last_name,
    validate_gender,
    validate_password,
    validate_email_edit,
    validate_profile_image,
)
from api.utils.error_messages import (
    error_code_401,
    error_code_402,
    error_code_404,
    error_code_405,
    error_code_405,
    error_code_1017,
)
from api.utils.middlewares import CustomIsAuthenticated


class UserRegistrationView(APIView):
    def post(self, request):
        try:

            email = request.data.get("email")
            password = request.data.get("password")
            first_name = request.data.get("firstName")
            last_name = request.data.get("lastName")
            phone_number = request.data.get("phoneNumber")
            dob = request.data.get("dob")
            gender = request.data.get("gender")
            profile_image = request.data.get("profileImage")

            validate_first_name(first_name)
            validate_last_name(last_name)
            validate_dob(dob)
            validate_email(email, True)
            validate_password(password)
            validate_phone_number(phone_number)
            validate_gender(gender)
            validate_profile_image(profile_image)

            user = UserData.objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                dob=dob,
                gender=gender,
                profile_image=profile_image,
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
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class UserLoginAPIView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            # Validate email and password
            validate_email(email, register=False)
            validate_password(password, "password")
            user = authenticate(request, email=email, password=password)

            if user is None:
                return Response(error_code_401(), status=status.HTTP_401_UNAUTHORIZED)

            refresh = RefreshToken.for_user(user)

            data = {
                "accessToken": str(refresh.access_token),
                "refreshToken": str(refresh),
                "userType": user.user_type,
            }

            return Response(data, status=status.HTTP_200_OK)

        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)


class GoogleLoginView(APIView):
    def post(self, request):
        try:
            # Get the token from the request
            token = request.data.get("token")
            if not token:
                return Response(
                    {"error": "Token is required."}, status=status.HTTP_400_BAD_REQUEST
                )

            client_id = config("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY")
            payload = id_token.verify_oauth2_token(token, requests.Request(), client_id)
            email = payload.get("email")
            user = UserData.objects.filter(email=email)
            name = payload.get("name")
            given_name = payload.get("given_name")
            picture = payload.get("picture")
            if user == None:
                user = UserData.objects.create_user(
                    email=email,
                    first_name=given_name,
                )

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
                "iat": int(current_time.timestamp()),
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
            return Response(error_code_402(), status=status.HTTP_401_UNAUTHORIZED)

        except GoogleAuthError as e:
            return Response(error_code_402(), status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AddStaffView(APIView):
    authentication_classes = (CustomIsAuthenticated,)
    permission_classes = (IsOwner,)

    def post(self, request, pk):
        try:
            email = request.data.get("email")
            password = request.data.get("password")
            first_name = request.data.get("firstName")
            last_name = request.data.get("lastName")
            phone_number = request.data.get("phoneNumber")
            dob = request.data.get("dob")
            gender = request.data.get("gender")
            profile_image = request.data.get("profileImage")

            validate_first_name(first_name)
            validate_last_name(last_name)
            validate_dob(dob)
            validate_email(email, True)
            validate_password(password, "password")
            validate_phone_number(phone_number)
            validate_gender(gender)
            validate_profile_image(profile_image)

            pharmacist = UserData.objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                dob=dob,
                gender=gender,
                profile_image=profile_image,
                user_type=3,
            )

            branch = Branch.objects.get(id=pk, status=1)
            branch.pharmacist_id = pharmacist
            branch.save()
            return Response(
                {"message": "User created successfully", "user_id": pharmacist.id},
                status=status.HTTP_200_OK,
            )
        except ValidationError as e:
            # Handle validation errors

            return Response(
                e.detail,
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class UserManagementView(APIView):
    authentication_classes = (CustomIsAuthenticated,)

    def put(self, request):
        try:
            user = request.user
            email = request.data.get("email", user.email)
            first_name = request.data.get("firstName", user.first_name)
            last_name = request.data.get("lastName", user.last_name)
            phone_number = request.data.get("phoneNumber", user.phone_number)
            dob = request.data.get("dob", user.dob)
            gender = request.data.get("gender", user.gender)
            profile_image = request.data.get("profileImage", user.profile_image)

            validate_first_name(first_name)
            validate_last_name(last_name)
            validate_dob(dob)
            validate_email_edit(email, user_id=user.id)
            validate_phone_number(phone_number)
            validate_gender(gender)
            validate_profile_image(profile_image)

            user.first_name = first_name, user.first_name
            user.last_name = last_name
            user.dob = dob
            user.email = email
            user.phone_number = phone_number
            user.gender = gender
            user.profile_image = profile_image

            user_obj = user.save()

            return Response(
                {"message": user_obj},
                status=status.HTTP_200_OK,
            )

        except ValidationError as e:
            # Handle validation errors
            return Response(
                e.detail,
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            # Handle other errors
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def patch(self, request):
        try:
            user = request.user
            current_password = request.data.get("currentPassword")
            new_password = request.data.get("newPassword")

            # Check if current password is correct
            if not user.check_password(current_password):
                return Response(
                    {"response": "Incorrect password"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Validate new password
            validate_password(current_password, "currentPassword")
            validate_password(new_password, "newPassword")

            # Set and save the new password
            user.set_password(new_password)
            user.save()

            return Response(
                {"message": "Password updated successfully"}, status=status.HTTP_200_OK
            )

        except ValidationError as e:
            # Handle validation errors (e.g., weak password)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # Handle other errors
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ForgotPasswordView(APIView):

    def post(self, request):
        try:
            email = request.data.get("email")
            user = UserData.objects.get(email=email)
            if user is None:
                return Response(error_code_1017(), status=status.HTTP_404_NOT_FOUND)
            if user.user_type != 2:
                return Response(error_code_405(), status=status.HTTP_403_FORBIDDEN)
            # generate token

            token = generate_reset_token(user.email, user.id)
            reset_password_link = f"/reset-password/token={token}"
            subject = f"{settings.APP_NAME} - Reset your password"
            template = "index.html"

            send_email(
                mail=user.email,
                subject=subject,
                template=template,
                user_name = user.first_name +" "+ user.last_name,
                url=reset_password_link,
                data={"username": user.first_name},
            )
            return Response(
                {"message": "Password reset link sent successfully"},
                status=status.HTTP_200_OK,
            )

        except UserData.DoesNotExist:
            return Response(
                error_code_1017,
                status=status.HTTP_400_BAD_REQUEST,
            )


class ResetPasswordAPIView(APIView):
    def post(self, request):
        try:
            token = request.query_params.get("token")
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])

            jti = payload.get("jti")

            if cache.get(jti):

                return Response(error_code_404, status=status.HTTP_401_UNAUTHORIZED)

            new_password = request.data.get("newPassword")
            validate_password(new_password, "newPassword")
            user = UserData.objects.get(id=payload["user_id"])

            if user.email != payload["email"]:
                data = error_code_402()
                return Response(
                    data,
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            user.set_password(new_password)
            user.save()

            # Mark the token as used by storing the jti in the cache
            cache.set(jti, True, timeout=None)

            return Response(
                {"message": "Password reset successfully"},
                status=status.HTTP_200_OK,
            )
        except ValidationError as e:
            return Response(
                e.detail,
                status=status.HTTP_400_BAD_REQUEST,
            )
        except jwt.ExpiredSignatureError:
            data = error_code_404()
            return Response(
                data,
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except jwt.exceptions.InvalidTokenError:
            data = error_code_402()
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
        
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
