from django.shortcuts import render

def home(request):
    return render(request,'djangoApp/django_home.html',{'active_nav': 'django'})

def intro(request):
    return render(request,'djangoApp/django_intro.html',{'active_page': 'introduction','active_nav': 'django'})

def venv(request):
    return render(request,'djangoApp/django_venv.html',{'active_page': 'venv','active_nav': 'django'})

def create(request):
    return render(request,'djangoApp/django_create.html',{'active_page': 'create','active_nav': 'django'})

def app(request):
    return render(request,'djangoApp/django_app.html',{'active_page': 'app','active_nav': 'django'})

def djfiles(request):
    return render(request,'djangoApp/django_files.html',{'active_page': 'djfiles','active_nav': 'django'})

def templates(request):
    return render(request,'djangoApp/django_templates.html',{'active_page': 'templates','active_nav': 'django'})