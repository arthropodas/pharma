from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import UserData
from api.utils.error_messages import error_code_1001,error_code_1002, error_code_1003, error_code_1004,error_code_1005,error_code_1006,error_code_1007,error_code_1008,error_code_1009, error_code_1010

class UserRegistrationViewTest(APITestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('user_registration')  # Update with your actual URL name
        
        self.valid_payload = {
            "email": "testuser@example.com",
            "password": "strongpassword123",
            "firstName": "John",
            "lastName": "Doe",
            "phoneNumber": "+1234567890",
            "dob": "2000-01-01",
            "userType": 2  # OWNER
        }

    def test_create_user_success(self):
        """Test creating a user with valid payload."""
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("user_id", response.data)
        self.assertEqual(UserData.objects.count(), 1)

    # def test_missing_required_fields(self):
    #     """Test creating a user with missing required fields."""
    #     invalid_payload = self.valid_payload.copy()
    #     invalid_payload.pop('firstName')
        
    #     response = self.client.post(self.url, invalid_payload, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(response.data, error_code_1001())

    # def test_invalid_email_format(self):
    #     """Test creating a user with invalid email format."""
    #     invalid_payload = self.valid_payload.copy()
    #     invalid_payload['email'] = 'invalidemail'
        
    #     response = self.client.post(self.url, invalid_payload, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(response.data, error_code_1004())

    # def test_duplicate_email(self):
    #     """Test creating a user with a duplicate email."""
    #     UserData.objects.create_user(
    #         email=self.valid_payload['email'],
    #         password="password123",
    #         first_name="Existing",
    #         last_name="User",
    #         phone_number="+1234567890",
    #         dob="1995-05-05",
    #         user_type=1
    #     )
        
    #     response = self.client.post(self.url, self.valid_payload, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(response.data, error_code_1010())

    # def test_invalid_user_type(self):
    #     """Test creating a user with invalid user type."""
    #     invalid_payload = self.valid_payload.copy()
    #     invalid_payload['userType'] = 5  # Invalid user type
        
    #     response = self.client.post(self.url, invalid_payload, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(response.data, error_code_1006())

    # def test_invalid_phone_number(self):
    #     """Test creating a user with an invalid phone number."""
    #     invalid_payload = self.valid_payload.copy()
    #     invalid_payload['phoneNumber'] = 'invalid-phone'
        
    #     response = self.client.post(self.url, invalid_payload, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(response.data, error_code_1007())

    # def test_invalid_last_name(self):
    #     """Test creating a user with invalid last name length."""
    #     invalid_payload = self.valid_payload.copy()
    #     invalid_payload['lastName'] = 'A'  # Too short
        
    #     response = self.client.post(self.url, invalid_payload, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(response.data, error_code_1008())

    # def test_invalid_dob_format(self):
    #     """Test creating a user with invalid date of birth format."""
    #     invalid_payload = self.valid_payload.copy()
    #     invalid_payload['dob'] = '01-01-2000'  # Invalid format
        
    #     response = self.client.post(self.url, invalid_payload, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(response.data, error_code_1009())
