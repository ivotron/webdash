from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.models import SocialToken, SocialAccount
from django.conf import settings
from apps.blackswan.serializers import WorkflowExecutionSerializer, \
                                       ProjectSerializer, \
                                       GithubRepoSerializer, \
                                       UserSerializer
from apps.blackswan.models import WorkflowExecution, Project, User
from apps.blackswan.permissions import IsOwnerOrPublic
from github import Github


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username=username).order_by('-id')
        else:
            queryset = queryset.filter(username=self.request.user.username).order_by('-id')
        return queryset


class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = settings.CALLBACK_URL
    client_class = OAuth2Client


class GitHubRepo(ListAPIView):
    serializer_class = GithubRepoSerializer

    def get_queryset(self):
        account = SocialAccount.objects.get(user=self.request.user)
        token = SocialToken.objects.get(account=account)
        g = Github(token.token)
        repos = [repo for repo in g.get_user().get_repos()
                 if not Project.objects.all().filter(github_id=repo.id).exists()]
        return repos


class SyncProjects(ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        account = SocialAccount.objects.get(user=self.request.user)
        token = SocialToken.objects.get(account=account)
        g = Github(token.token)
        repos = [Project.objects.all().filter(github_id=repo.id)
                 .exclude(user__id=self.request.user.id).first()
                 for repo in g.get_user().get_repos()]
        repos = [repo for repo in repos if repo is not None]
        for repo in repos:
            repo.user.add(self.request.user)
        return repos


class ProjectViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrPublic]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_serializer_context(self):
        return { 'request':self.request }

    def get_queryset(self):
        queryset = Project.objects.all()
        user = self.request.query_params.get('username', None)
        if user is not None:
            queryset = queryset.filter(user__username=user).filter(private=False).order_by('-id')
        else:
            queryset = queryset.filter(user=self.request.user.id).order_by('-id')
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=[self.request.user])


class WorkflowExecutionViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrPublic]
    queryset = WorkflowExecution.objects.all()
    serializer_class = WorkflowExecutionSerializer

    def get_queryset(self):
        queryset = WorkflowExecution.objects.all()
        project_repo = self.request.query_params.get('project', None)
        if project_repo is not None:
            queryset = queryset.filter(
                project__repo=project_repo).order_by('-id')
        return queryset
