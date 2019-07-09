from rest_framework.authtoken.models import Token
from apps.users.models import User
from rest_framework.test import APITestCase
from rest_framework.test import APIClient


class UserAuthAPITestCase(APITestCase):
    fixtures = ['users.json']

    def test_valid_user(self):
        client = APIClient()
        response = client.post('/auth/login/', {'email': 'popper@blackswan.me', 'password': 'password'}, format='json')
        token = Token.objects.get(user__email='popper@blackswan.me')
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        self.assertEqual(response.status_code, 200)

    def test_invalid_user(self):
        client = APIClient()
        response = client.post('/auth/login/', {'email': 'popper@blkswan.me', 'password': 'password'}, format='json')
        self.assertEqual(response.status_code, 400)
