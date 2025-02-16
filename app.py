import os
import django
from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.management import execute_from_command_line


settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],
    INSTALLED_APPS=[
        'django.contrib.contenttypes',
        'django.contrib.auth',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ],
    STATIC_URL='/static/',
)


django.setup()


def home(request):
    return HttpResponse("<h1>Hello, Django in a single file!</h1>")


urlpatterns = [path('', home),]


if __name__ == "__main__":
    execute_from_command_line(['manage.py', 'runserver', '127.0.0.1:8000'])