from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from apps.blackswan.serializers import WorkflowExecutionSerializer, \
                                       ProjectSerializer
from apps.blackswan.models import WorkflowExecution, Project


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def list(self, request):
        queryset = Project.objects.filter(user=request.user.id).order_by('-id')
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

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
