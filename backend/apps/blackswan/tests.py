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
        if response.status_code is not 200:
            raise AssertionError("Api not responding, test failed.")
        else:
            print("API responded with 200 code")

    def test_user_projects_login(self):
        print("\nTest: Project query user:")
        client = APIClient()
        client.post('/auth/login/', {'email': 'popper@blackswan.me', 'password': 'password'}, format='json')
        response = client.get('/api/projects/', {})
        print("Response: ")
        if response.data is None:
            raise AssertionError("Response missing data, test failed.")
        else:
            print(response.data)

class ExecutionAPITestCase(APITestCase):
    fixtures = ['users.json', 'projects.json', 'executions.json']

    def test_executions_project_query(self):
        print("\nTest: Execution query null project:")
        client = APIClient()
        response = client.get('/api/executions?project=null_test', {})
        print(response)
        if response.status_code is not 200:
            raise AssertionError("Api not responding, test failed.")
        else:
            print("API responded with 200 code")

    def test_executions_project(self):
        print("\nTest: Execution query:")
        client = APIClient()
        response = client.get('/api/executions?project=project_test', {})
        if response.data is None:
            raise AssertionError("Response missing data, test failed.")
        else:
            print(response.data)
