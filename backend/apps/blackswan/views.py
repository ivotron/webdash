from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from apps.blackswan.serializers import WorkflowExecutionSerializer, \
                                       ProjectSerializer
from apps.blackswan.models import WorkflowExecution, Project
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.conf import settings
from rest_framework.generics import ListAPIView


class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = settings.CALLBACK_URL
    client_class = OAuth2Client


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.all()
        user = self.request.query_params.get('username', None)
        if user is not None:
            queryset = queryset.filter(user__username=user).order_by('-id')
        else:
            queryset = queryset.filter(user=self.request.user.id).order_by('-id')
        return queryset

class WorkflowExecutionViewSet(ModelViewSet):
    queryset = WorkflowExecution.objects.all()
    serializer_class = WorkflowExecutionSerializer

    def get_queryset(self):
        queryset = WorkflowExecution.objects.all()
        project_title = self.request.query_params.get('project', None)
        if project_title is not None:
            queryset = queryset.filter(
                project__title=project_title).order_by('-id')
        return queryset
