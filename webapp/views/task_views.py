from django.shortcuts import render, get_object_or_404, redirect, reverse
from webapp.models import Task, Project
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import TaskForm
from django.urls import reverse_lazy

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_view.html'

class TaskCreateView(CreateView):
    form_class = TaskForm
    template_name = 'tasks/create_task.html'

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        form.save_m2m()
        return redirect('webapp:detail_project', pk=project.pk)

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'

    def get_success_url(self):
        return reverse('webapp:detail_project', kwargs={'pk': self.object.project.pk})

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update_task.html'

    def get_success_url(self):
        return reverse('webapp:task_view', kwargs={'pk': self.object.pk})