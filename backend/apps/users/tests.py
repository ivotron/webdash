from rest_framework.authtoken.models import Token
from apps.users.models import User
from rest_framework.test import APITestCase
from rest_framework.test import APIClient


class UserAuthAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(id=1, email='popper@blackswan.me',
                            password='password')
        user.set_password('password')
        user.save()
        self.user = user

    def test_valid_user(self):
        client = APIClient()
        response = client.post('/auth/login/', {'email': self.user.email,
                                                'password': 'password'},
                               format='json')
        token = Token.objects.get(user__email=self.user.email)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        self.assertEqual(response.status_code, 200)

    def test_invalid_user(self):
        client = APIClient()
        response = client.post('/auth/login/', {'email': 'popper@blkswan.me',
                                                'password': 'password'},
                               format='json')
        self.assertEqual(response.status_code, 400)
