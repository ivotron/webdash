from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from apps.blackswan.models import Project, WorkflowExecution
from apps.blackswan.views import WorkflowExecutionViewSet, ProjectViewSet
import json


class ProjectAPITestCase(APITestCase):
    fixtures = ['users.json', 'projects.json']

    def test_user_projects(self):
        client = APIClient()
        response = client.get('/api/projects/', {})
        self.assertEqual(response.status_code, 200)

    def test_user_projects_login(self):
        data = Project.objects.all()
        data_json = [{'id':obj.id, 'title':obj.title, 'repo_url':obj.repo_url,
                      'user':obj.user.id} for obj in data]
        client = APIClient()
        client.post('/auth/login/', {'email': 'popper@blackswan.me',
                                     'password': 'password'}, format='json')
        response = client.get('/api/projects/', {})
        print(data_json)
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.data, data_json)

class ExecutionAPITestCase(APITestCase):
    fixtures = ['users.json', 'projects.json', 'executions.json']

    def test_executions_project_query(self):
        client = APIClient()
        response = client.get('/api/executions?project=null_test', {})
        self.assertEqual(response.status_code, 200)

    def test_executions_project(self):
        #data = b'[{"id":1,"revision":"76D7SF687D6SF","branch":"master","state":"running","pr":"https://github.com/johndoe/project_1/pull/5","ci_url":"https://travis-ci.org/systemslab/popper/builds/538372099?utm_source=github_status&utm_medium=notification","wf_str":"workflow \\"cli tests\\" {\\r\\n  on = \\"push\\"\\r\\n  resolves = \\"end\\"\\r\\n}\\r\\naction \\"lint\\" {\\r\\n  uses = \\"actions/bin/shellcheck@master\\"\\r\\n  args = \\"./ci/test/*\\"\\r\\n}","wf_json":"NA","log":"NA","exec_date":"2019-05-22","exec_number":1,"project":1}]'
        view = ProjectViewSet.as_view({'get': 'retrieve'})
        client = APIRequestFactory()
        request = client.get('/api/executions?project=project_test')
        response = view(request, pk=1)
        response.render()
        self.assertEqual(response.status_code, 200)
        print(response.content)
