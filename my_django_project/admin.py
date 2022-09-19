from django.contrib import admin


class MyDjangoProjectAdminSite(admin.AdminSite):
    site_title = "BookBout Admin Site"
    site_header = "Welcome to the BookBout Admin InterFace"
    index_title = "BookBout Index"
