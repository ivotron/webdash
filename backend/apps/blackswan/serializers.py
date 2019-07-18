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
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    def create(self, validated_data):
        #validated_data['user'] = self.request.user.id
        project = Project.objects.create(
            organization = validated_data['organization'],
            private = validated_data['private'],
            repo = validated_data['repo'],
            repo_url = validated_data['repo_url'],
            github_id = validated_data['github_id'],
        )
        return project

    class Meta:
        read_only_fields = ('last_execution',)
        model = Project
        fields = '__all__'


class OwnerSerializer(serializers.Serializer):
    organizations_url = serializers.CharField(max_length=200)


class GithubRepoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    html_url = serializers.CharField(max_length=200)
    owner = OwnerSerializer()
    id  = serializers.IntegerField()
    private = serializers.BooleanField()
