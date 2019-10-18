from rest_framework import routers
from apps.blackswan.views import ProjectViewSet, \
                                 WorkflowExecutionViewSet, \
                                 UserViewSet

# Settings
api = routers.DefaultRouter()
api.trailing_slash = '/?'

# APIs
api.register(r'users', UserViewSet)
api.register(r'projects', ProjectViewSet, basename='Project')
api.register(r'executions', WorkflowExecutionViewSet)
