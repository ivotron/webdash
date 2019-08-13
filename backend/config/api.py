from rest_framework import routers
from apps.blackswan.views import ProjectViewSet, \
                                 WorkflowExecutionViewSet

# Settings
api = routers.DefaultRouter()
api.trailing_slash = '/?'

# APIs
api.register(r'projects', ProjectViewSet)
api.register(r'executions', WorkflowExecutionViewSet)
