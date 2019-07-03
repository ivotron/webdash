from rest_framework.serializers import ModelSerializer
from apps.users.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username')
        read_only_fields = ('email', 'username')
