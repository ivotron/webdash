from uuid import uuid4
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, \
                                       PermissionsMixin
from django.db import models
from django.utils import timezone
import logging
logger = logging.getLogger(__name__)



class UserManager(BaseUserManager):
    def _create_user(
            self,
            email,
            password,
            is_staff,
            is_superuser,
            **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        user = self.model(email=self.normalize_email(email),
                          is_active=True,
                          is_staff=is_staff,
                          is_superuser=is_superuser,
                          last_login=timezone.now(),
                          registered_at=timezone.now(),
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        is_staff = extra_fields.pop('is_staff', False)
        is_superuser = extra_fields.pop('is_superuser', False)
        return self._create_user(
            email,
            password,
            is_staff,
            is_superuser,
            **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(
            email,
            password,
            is_staff=True,
            is_superuser=True,
            **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='Email',
        unique=True,
        max_length=255)
    full_name = models.CharField(
        verbose_name='Full name',
        max_length=30,
        default='name')
    avatar = models.ImageField(verbose_name='Avatar', blank=True)
    token = models.UUIDField(
        verbose_name='Token',
        default=uuid4,
        editable=False)
    username = models.CharField(
        verbose_name='Username',
        max_length=30,
        editable=False,
        default="_"
    )
    is_admin = models.BooleanField(verbose_name='Admin', default=False)
    is_active = models.BooleanField(verbose_name='Active', default=True)
    is_staff = models.BooleanField(verbose_name='Staff', default=False)
    registered_at = models.DateTimeField(
        verbose_name='Registered at',
        auto_now_add=timezone.now)

    # Fields settings
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.CharField(max_length=256, default="NA")
    private = models.BooleanField(default=False)
    repo = models.CharField(max_length=256, default="NA")
    repo_url = models.CharField(max_length=256, default="NA")
    enabled = models.BooleanField(default=False)

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
    actor = models.CharField(max_length=256, default="NA")
