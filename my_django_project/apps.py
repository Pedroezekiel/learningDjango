from django.contrib.admin.apps import AdminConfig


class MyDjangoAdminConfig(AdminConfig):
    default_site = 'my_django_project.admin.MyDjangoProjectAdminSite'
