from rest_framework import serializers
from apps.blackswan.models import WorkflowExecution, Project


class WorkflowExecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkflowExecution
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    last_execution = WorkflowExecutionSerializer(source='latest_execution',
                                                 read_only=True)
    class Meta:
        read_only_fields = ('last_execution',)
        model = Project
        fields = '__all__'
