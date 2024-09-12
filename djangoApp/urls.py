from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='dj_home'),
    path('introduction/', views.intro,name='django_intro'),
    path('virtual-environment/', views.venv,name='django_venv'),
    path('create-project/', views.create,name='django_create'),
    path('django-app/', views.app,name='django_app'),
    path('django-files/', views.djfiles,name='django_files'),
    path('django-templates/', views.templates,name='django_templates'),
]
