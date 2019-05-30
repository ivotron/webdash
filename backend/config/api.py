from rest_framework import routers
from apps.users.views import UserViewSet
from apps.blackswan.views import WorkflowExecutionViewSet

# Settings
api = routers.DefaultRouter()
api.trailing_slash = '/?'

# APIs
api.register(r'users', UserViewSet)
api.register(r'executions', WorkflowExecutionViewSet)
