from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task
from django.views.generic import View, TemplateView
from webapp.forms import TaskForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class TaskView(TemplateView):
    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = get_object_or_404(Task, pk=kwargs.get('pk'))
        return context


class TaskCreateView(View):
    def get(self, requset, *args, **kwargs):
        form = TaskForm()
        return render(requset, 'create_task.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop('type')
            task = Task.objects.create(
                summary=form.cleaned_data.get('summary'),
                description=form.cleaned_data.get('description'),
                status=form.cleaned_data.get('status'),
            )
            task.type.set(types)
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'create_task.html', {'form': form})


class TaskUpdateView(TemplateView):
    template_name = 'update_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        form = TaskForm(initial={
            'summary': task.summary,
            'description': task.description,
            'status': task.status,
            'type': task.type.all(),
        })
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        form = TaskForm(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop('type')
            task.summary = form.cleaned_data.get('summary')
            task.description = form.cleaned_data.get('description')
            task.status = form.cleaned_data.get('status')
            task.type.set(types)
            task.save()
            return redirect('home')
        else:
            task.save()
            return render(request, 'update_task.html', {'form': form})

class TaskDeleteView(View):
    def get(self, requset, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        return render(requset, 'task_delete.html', {'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task.delete()
        return redirect('home')
