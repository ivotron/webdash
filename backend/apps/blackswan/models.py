from django.db import models
from django.utils import timezone
from apps.users.models import User
import logging
logger = logging.getLogger(__name__)

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #org
    #repo
    title = models.CharField(max_length=256, default="NA")
    repo_url = models.CharField(max_length=256, default="NA")

    @property
    def latest_execution(self):
        return self.workflowexecution_set.all().order_by('-id').first()


class WorkflowExecution(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    revision = models.CharField(max_length=256, default="NA")
    branch = models.CharField(max_length=256, default="NA")
    state = models.CharField(default='running', max_length=256)
    pr = models.CharField(max_length=256, default="NA")
    ci_url = models.CharField(max_length=2048, default="NA")
    wf_str = models.TextField(default="NA")
    wf_json = models.TextField(default="NA")
    log = models.TextField(default="NA")
    exec_date = models.DateField(default=timezone.now, blank=True, null=True)
    exec_number = models.IntegerField(default=0)
