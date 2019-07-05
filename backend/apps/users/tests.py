from rest_framework.authtoken.models import Token
from apps.users.models import User
from rest_framework.test import APITestCase
from rest_framework.test import APIClient


class UserAuthAPITestCase(APITestCase):
    fixtures = ['users.json']
    def test_user_exists(self):
        user = User.objects.get(email='popper@blackswan.me')

    def test_valid_user(self):
        client = APIClient()
        response = client.post('/auth/login/', {'email': 'popper@blackswan.me', 'password': 'password'}, format='json')
        print(Token.objects.first().user.email)
        token = Token.objects.get(user__email='popper@blackswan.me')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_invalid_user(self):
        client = APIClient()
        response = client.post('/auth/login/', {'email': 'popper5@blackswan.me', 'password': 'password'}, format='json')
        if(response.status_code is not '200'):
            print('Test failed succesfully!')
        else:
            print('Test failed.')
