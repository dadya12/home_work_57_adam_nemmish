"""
URL configuration for task project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from webapp.views.project_view import (ProjectListView, ProjectDetailView, ProjectCreateView,
                                       ProjectUpdateView, ProjectDeleteView)
from webapp.views.task_views import TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProjectListView.as_view(), name='home'),
    path('project/', RedirectView.as_view(pattern_name='home')),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='detail_project'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='update_project'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='delete_project'),
    path('projects/add/', ProjectCreateView.as_view(), name='create_project'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_view'),
    path('task/<int:pk>/add/', TaskCreateView.as_view(), name='create_task'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='update_task'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='delete_task'),
]
