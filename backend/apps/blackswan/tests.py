from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from apps.users.models import User
from apps.blackswan.models import Project, WorkflowExecution
import json


class ProjectAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(id=1, email='popper@blackswan.me',
                            password='password')
        user.set_password('password')
        user.save()
        self.user = user
        user2 = User.objects.create(id=2, email='popper2@blackswan.me',
                            password='password')
        user2.set_password('password')
        user2.save()
        self.user2 = user2
        project = Project.objects.create(id=1, user=User.objects.get(id=1),
            title="project_test",
            repo_url="https://github.com/johndoe/project_test.git"
        )
        self.project = project
        project.save()
        project2 = Project.objects.create(id=2, user=User.objects.get(id=2),
            title="project_test2",
            repo_url="https://github.com/johndoe/project_test2.git"
        )
        self.project2 = project2
        project2.save()
        execution = WorkflowExecution.objects.create(id=1, project=Project.objects.get(id=2),
            revision='76D7SF687D6SF', branch='master', state='running',
            pr='https://github.com/johndoe/project_1/pull/5',
            ci_url='https://travis-ci.org/systemslab/popper/builds/538372099?utm_source=github_status&utm_medium=notification',
            wf_str='workflow \"cli tests\" {\r\n  on = \"push\"\r\n  resolves = \"end\"\r\n}\r\naction \"lint\" {\r\n  uses = \"actions/bin/shellcheck@master\"\r\n  args = \"./ci/test/*\"\r\n}',
            wf_json='NA', log='NA', exec_date='2019-05-22', exec_number=1
        )
        self.execution = execution
        execution.save()

    def test_user_projects(self):
        client = APIClient()
        response = client.get('/api/projects/', {})
        self.assertEqual(response.status_code, 200)

    def test_user_projects_login(self):
        client = APIClient()
        log = client.post('/auth/login/', {'email': self.user.email,
                                     'password': 'password'}, format='json')
        response = client.get('/api/projects/', {})
        response.render()
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, [{'id':self.project.id,
                                                'last_execution':getattr(self.project, "last_execution", None),
                                                'repo_url':self.project.repo_url,
                                                'title':self.project.title,
                                                'user':self.project.user.id}])

    def test_executions_project_query(self):
        client = APIClient()
        response = client.get('/api/executions?project=null_test', {})
        self.assertEqual(response.status_code, 200)

    def test_executions_project(self):
        client = APIClient()
        response = client.get('/api/executions?project=project_test2')
        response.render()
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, [{'id':self.execution.id,
                                                'revision':self.execution.revision,
                                                'branch':self.execution.branch,
                                                'state':self.execution.state,
                                                'pr':self.execution.pr,
                                                'ci_url':self.execution.ci_url,
                                                'wf_str':self.execution.wf_str,
                                                'wf_json':self.execution.wf_json,
                                                'log':self.execution.log,
                                                'exec_date':self.execution.exec_date,
                                                'exec_number':self.execution.exec_number,
                                                'project':self.execution.project.id,
                                                }])
