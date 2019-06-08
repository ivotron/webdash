from rest_framework.serializers import ModelSerializer
from apps.blackswan.models import WorkflowExecution, Project

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class WorkflowExecutionSerializer(ModelSerializer):
    class Meta:
        model = WorkflowExecution
        fields = '__all__'
