from django.urls import path
from webapp.views.project_view import (ProjectListView, ProjectDetailView, ProjectCreateView,
                                       ProjectUpdateView, ProjectDeleteView)
from webapp.views.task_views import TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView
from django.views.generic import RedirectView

app_name = 'webapp'

urlpatterns = [
    path('', ProjectListView.as_view(), name='home'),
    path('project/', RedirectView.as_view(pattern_name='webapp:home')),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='detail_project'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='update_project'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='delete_project'),
    path('projects/add/', ProjectCreateView.as_view(), name='create_project'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_view'),
    path('task/<int:pk>/add/', TaskCreateView.as_view(), name='create_task'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='update_task'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='delete_task'),
]