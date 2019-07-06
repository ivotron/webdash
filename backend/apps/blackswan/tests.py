from rest_framework.authtoken.models import Token
from apps.users.models import User
from rest_framework.test import APITestCase
from rest_framework.test import APIClient


class ProjectAPITestCase(APITestCase):
    fixtures = ['users.json', 'projects.json']

    def test_user_projects(self):
        print("\nTest: Project query:")
        client = APIClient()
        response = client.get('/api/projects/', {})
        print("Response: ")
        print(response)


    def test_user_projects_login(self):
        print("\nTest: Project query user:")
        client = APIClient()
        client.post('/auth/login/', {'email': 'popper@blackswan.me', 'password': 'password'}, format='json')
        response = client.get('/api/projects/', {})
        print("Response: ")
        print(response.data)


class ExecutionAPITestCase(APITestCase):
    fixtures = ['users.json', 'projects.json', 'executions.json']

    def test_executions_project(self):
        print("\nTest: Execution query:")
        client = APIClient()
        response = client.get('/api/executions?project=project_test', {})
        print("Response: ")
        print(response.data)

    def test_executions_project_null(self):
        print("\nTest: Execution query null project:")
        client = APIClient()
        response = client.get('/api/executions?project=null_test', {})
        print("Response: ")
        print(response.data)
