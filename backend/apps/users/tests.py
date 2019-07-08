from rest_framework.authtoken.models import Token
from apps.users.models import User
from rest_framework.test import APITestCase
from rest_framework.test import APIClient


class UserAuthAPITestCase(APITestCase):
    fixtures = ['users.json']

    def test_user_exists(self):
        print("\nTest: User exists")
        user = User.objects.get(email='popper@blackswan.me')
        print(user)

    def test_valid_user(self):
        print("\nTest: Valid user login")
        client = APIClient()
        response = client.post('/auth/login/', {'email': 'popper@blackswan.me', 'password': 'password'}, format='json')
        print(Token.objects.first().user.email)
        token = Token.objects.get(user__email='popper@blackswan.me')
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        if response.status_code is not 200:
            raise AssertionError("Login failed.")
        else:
            print("Test succesful")

    def test_invalid_user(self):
        print("\nTest: Invalid user login")
        client = APIClient()
        response = client.post('/auth/login/', {'email': 'popper@blkswan.me', 'password': 'password'}, format='json')
        if response.status_code is '200':
            raise AssertionError("Could login with invalid user, test failed")
        else:
            print('Test failed succesfully.')
