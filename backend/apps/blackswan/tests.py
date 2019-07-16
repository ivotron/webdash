from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from apps.blackswan.models import Project, WorkflowExecution, User


class QuerysTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(id=1, email='popper@blackswan.me',
                            password='password',
                            username='JohnDoe')
        user.set_password('password')
        user.save()
        self.user = user

        user2 = User.objects.create(id=2, email='popper2@blackswan.me',
                            password='password',
                            username='JohnDrapper')
        user2.set_password('password')
        user2.save()
        self.user2 = user2

        user3 = User.objects.create(id=3, email='popper3@blackswan.me',
                            password='password',
                            username='Stavros')
        user3.set_password('password')
        user3.save()
        self.user3 = user3

        project = Project.objects.create(id=1, user=User.objects.get(id=1),
            title="project_test",
            repo_url="https://github.com/johndoe/project_test.git",
            private=False
        )
        self.project = project
        project.save()

        project2 = Project.objects.create(id=2, user=User.objects.get(id=1),
            title="project_test2",
            repo_url="https://github.com/johndoe/project_test2.git",
            private=True
        )
        self.project2 = project2
        project2.save()

        project3 = Project.objects.create(id=3, user=User.objects.get(id=2),
            title="project_test3",
            repo_url="https://github.com/johndoe/project_test3.git",
            private=False
        )
        self.project3 = project3
        project3.save()

        project4 = Project.objects.create(id=4, user=User.objects.get(id=2),
            title="project_test4",
            repo_url="https://github.com/johndoe/project_test4.git",
            private=True
        )
        self.project4 = project4
        project4.save()

        project5 = Project.objects.create(id=5, user=User.objects.get(id=3),
            title="project_test5",
            repo_url="https://github.com/johndoe/project_test5.git",
            private=False
        )
        self.project5 = project5
        project5.save()

        project6 = Project.objects.create(id=6, user=User.objects.get(id=3),
            title="project_test6",
            repo_url="https://github.com/johndoe/project_test6.git",
            private=True
        )
        self.project6 = project6
        project6.save()

        execution = WorkflowExecution.objects.create(id=1, project=Project.objects.get(id=5),
            revision='76D7SF687D6SF', branch='master', state='running',
            pr='https://github.com/johndoe/project_5/pull/5',
            ci_url='https://travis-ci.org/systemslab/popper/builds/538372099?utm_source=github_status&utm_medium=notification',
            wf_str='workflow \"cli tests\" {\r\n  on = \"push\"\r\n  resolves = \"end\"\r\n}\r\naction \"lint\" {\r\n  uses = \"actions/bin/shellcheck@master\"\r\n  args = \"./ci/test/*\"\r\n}',
            wf_json='NA', log='NA', exec_date='2019-05-22', exec_number=1
        )
        self.execution = execution
        execution.save()

        execution2 = WorkflowExecution.objects.create(id=2, project=Project.objects.get(id=6),
            revision='76D7SF687D6SF', branch='master', state='running',
            pr='https://github.com/johndoe/project_6/pull/5',
            ci_url='https://travis-ci.org/systemslab/popper/builds/538372099?utm_source=github_status&utm_medium=notification',
            wf_str='workflow \"cli tests\" {\r\n  on = \"push\"\r\n  resolves = \"end\"\r\n}\r\naction \"lint\" {\r\n  uses = \"actions/bin/shellcheck@master\"\r\n  args = \"./ci/test/*\"\r\n}',
            wf_json='NA', log='NA', exec_date='2019-05-22', exec_number=1
        )
        self.execution2 = execution2
        execution2.save()

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

    def test_user_projects(self):
        client = APIClient()
        response = client.get('/api/projects/')
        self.assertEqual(response.status_code, 200)

    def test_user_projects_private(self):
        client = APIClient()
        client.post('/auth/login/', {'email': self.user2.email,
                                     'password': 'password'}, format='json')
        token = Token.objects.get(user__email=self.user2.email)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/api/projects/')
        response.render()
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, [{'id':self.project4.id,
                                                 'last_execution':getattr(self.project4, "last_execution", None),
                                                 'repo_url':self.project4.repo_url,
                                                 'title':self.project4.title,
                                                 'user':self.project4.user.id,
                                                 'organization':self.project4.organization,
                                                 'private':self.project4.private
                                                },
                                                {'id':self.project3.id,
                                                'last_execution':getattr(self.project3, "last_execution", None),
                                                'repo_url':self.project3.repo_url,
                                                'title':self.project3.title,
                                                'user':self.project3.user.id,
                                                'organization':self.project3.organization,
                                                'private':self.project3.private
                                                }
                                                ])

    def test_project_public(self):
        client = APIClient()
        response = client.get('/api/projects?username=JohnDoe')
        response.render()
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, [{'id':self.project.id,
                                                'last_execution':getattr(self.project, "last_execution", None),
                                                'repo_url':self.project.repo_url,
                                                'title':self.project.title,
                                                'user':self.project.user.id,
                                                'organization':self.project.organization,
                                                'private':self.project.private}])

    def test_executions_project_query(self):
        client = APIClient()
        response = client.get('/api/executions?project=null_test')
        self.assertEqual(response.status_code, 200)


    def test_executions_project_public(self):
        client = APIClient()
        response = client.get('/api/executions?project=project_test5')
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
                                                 'username_pr':self.execution.username_pr
                                                }])

    def test_executions_project_private(self):
        client = APIClient()
        client.post('/auth/login/', {'email': self.user3.email,
                                     'password': 'password'}, format='json')
        token = Token.objects.get(user__email=self.user3.email)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/api/executions?project=project_test6')
        response.render()
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, [{'id':self.execution2.id,
                                                 'revision':self.execution2.revision,
                                                 'branch':self.execution2.branch,
                                                 'state':self.execution2.state,
                                                 'pr':self.execution2.pr,
                                                 'ci_url':self.execution2.ci_url,
                                                 'wf_str':self.execution2.wf_str,
                                                 'wf_json':self.execution2.wf_json,
                                                 'log':self.execution2.log,
                                                 'exec_date':self.execution2.exec_date,
                                                 'exec_number':self.execution2.exec_number,
                                                 'project':self.execution2.project.id,
                                                 'username_pr':self.execution2.username_pr
                                                }])
