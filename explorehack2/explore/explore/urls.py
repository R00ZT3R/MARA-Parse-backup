"""explore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from leads.views import IndexView
from leads.views import QuestionView
from leads.views import AboutView
from leads import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('question/', QuestionView.as_view(), name='question'),
    path('result/', views.result_upload, name='result_upload'),
    path('question/result/', views.question_upload, name='question_upload'),
    path('about/', AboutView.as_view(), name='about'),
]
