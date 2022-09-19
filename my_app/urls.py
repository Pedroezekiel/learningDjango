from django.urls import path
from . import views

app_name ='my_app'

urlpatterns = [
    path(' ', views.index, name='index'),
    path('redirect/', views.redirect),
    path('about/', views.about, name='about'),
    # path()
]
