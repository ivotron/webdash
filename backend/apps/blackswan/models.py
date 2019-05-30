from django.db import models
from django.utils import timezone

class WorkflowExecution(models.Model):
    revision = models.CharField(max_length=256)
    branch = models.CharField(max_length=256)
    pr = models.CharField(max_length=256)
    ci_url = models.CharField(max_length=2048)
    repo_url = models.CharField(max_length=2048)
    wf_str = models.TextField(max_length=2500)
    exec_date = models.DateField(default=timezone.now, blank=True, null=True)
