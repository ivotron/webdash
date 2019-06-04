from rest_framework.serializers import ModelSerializer
from apps.blackswan.models import WorkflowExecution


class WorkflowExecutionSerializer(ModelSerializer):
    class Meta:
        model = WorkflowExecution
        fields = '__all__'
