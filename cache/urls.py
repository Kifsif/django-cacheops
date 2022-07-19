"""cache URL Configuration

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

from polls.views import QuestionDetailView, QuestionList, PollList, PollDetailView

urlpatterns = [
    path('admin/clearcache/', include('clearcache.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name="question"),
    path('questions/list/', QuestionList.as_view(), name="question_list"),
    path('polls/<int:pk>/', PollDetailView.as_view(), name="poll"),
    path('polls/list/', PollList.as_view(), name="polls_list"),
]
