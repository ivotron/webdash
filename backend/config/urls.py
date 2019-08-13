from django.urls import path
from django.contrib import admin
from django.contrib.auth import logout
from django.conf.urls import include, url
from config.api import api
from apps.blackswan.views import GitHubLogin, GitHubRepo, SyncProjects, UserViewSet
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('logout/', logout, {'next_page': '/'}, name='logout'),
    path('api/', include(api.urls)),
    url(r'^accounts/', include('allauth.urls'), name='socialaccount_signup'),
    url(r'^auth/github/?$', GitHubLogin.as_view(), name='github_login'),
    url(r'^auth/github/repo/?$', GitHubRepo.as_view(), name='github_repo'),
    url(r'^auth/github/repo/sync/?$', SyncProjects.as_view(), name='github_sync'),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls'))
]
