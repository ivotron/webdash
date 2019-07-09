from rest_framework.authtoken.models import Token
from apps.users.models import User
from rest_framework.test import APITestCase
from rest_framework.test import APIClient


class ProjectAPITestCase(APITestCase):
    fixtures = ['users.json', 'projects.json']

    def test_user_projects(self):
        client = APIClient()
        response = client.get('/api/projects/', {})
        self.assertEqual(response.status_code, 200)

    def test_user_projects_login(self):
        client = APIClient()
        client.post('/auth/login/', {'email': 'popper@blackswan.me', 'password': 'password'}, format='json')
        response = client.get('/api/projects/', {})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

class ExecutionAPITestCase(APITestCase):
    fixtures = ['users.json', 'projects.json', 'executions.json']

    def test_executions_project_query(self):
        client = APIClient()
        response = client.get('/api/executions?project=null_test', {})
        self.assertEqual(response.status_code, 200)

    def test_executions_project(self):
        client = APIClient()
        response = client.get('/api/executions?project=project_test', {})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)
