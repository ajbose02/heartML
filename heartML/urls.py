"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'heartML'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('survey', views.survey, name='survey'),
    path('prediction/<int:a>/<int:b>/<int:c>/<int:d>/<int:e>/<int:f>/<int:g>/<int:h>/<int:i>/<int:j>/<int:k>/<int:l>/<int:m>/<int:n>/<int:o>/<int:p>/<int:q>/', views.prediction, name="prediction"),
    path('prediction/', views.pred, name="pred"),
    path('goals/', views.goals, name="goals"),
    path('users/', include('users.urls')),
]
