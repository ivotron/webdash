from rest_framework.viewsets import ModelViewSet
from apps.blackswan.serializers import WorkflowExecutionSerializer
from apps.blackswan.models import WorkflowExecution


class WorkflowExecutionViewSet(ModelViewSet):
    queryset = WorkflowExecution.objects.all()
    serializer_class = WorkflowExecutionSerializer
