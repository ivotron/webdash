from rest_framework import serializers
from apps.blackswan.models import User, WorkflowExecution, Project


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username')
        read_only_fields = ('email', 'username')


class WorkflowExecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkflowExecution
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    last_execution = WorkflowExecutionSerializer(source='latest_execution',
                                                 read_only=True)
    user = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        read_only = ['user']
        fields = ['id', 'organization', 'private', 'repo', 'repo_url',
                  'github_id', 'user', 'last_execution', 'enabled']


class OwnerSerializer(serializers.Serializer):
    organizations_url = serializers.CharField(max_length=200)


class GithubRepoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    html_url = serializers.CharField(max_length=200)
    owner = OwnerSerializer()
    id  = serializers.IntegerField()
    private = serializers.BooleanField()
