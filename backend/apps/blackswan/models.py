from django.db import models
from django.utils import timezone
from apps.users.models import User
import logging
logger = logging.getLogger(__name__)

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #org
    #repo
    title = models.CharField(max_length=256)
    repo_url = models.CharField(max_length=256)

    @property
    def latest_execution(self):
        return self.workflowexecution_set.all().order_by('-id').first()


class WorkflowExecution(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    revision = models.CharField(max_length=256)
    branch = models.CharField(max_length=256)
    state = models.CharField(default='running', max_length=256)
    pr = models.CharField(max_length=256)
    ci_url = models.CharField(max_length=2048)
    wf_str = models.TextField()
    wf_json = models.TextField()
    log = models.TextField()
    exec_date = models.DateField(default=timezone.now, blank=True, null=True)
    exec_number = models.IntegerField(default=0)
