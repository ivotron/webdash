from rest_framework.viewsets import ModelViewSet
from apps.blackswan.serializers import WorkflowExecutionSerializer
from apps.blackswan.models import WorkflowExecution
from apps.blackswan.serializers import ProjectSerializer
from apps.blackswan.models import Project


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class WorkflowExecutionViewSet(ModelViewSet):
    queryset = WorkflowExecution.objects.all()
    serializer_class = WorkflowExecutionSerializer
