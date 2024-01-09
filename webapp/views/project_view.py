from urllib.parse import urlencode
from django.shortcuts import reverse, redirect
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from webapp.forms import SimpleSearchForm, ProjectForm, ProjectUserForm
from webapp.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/home.html'
    context_object_name = 'projects'
    paginate_by = 5

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.search_form.is_valid():
            return self.search_form.cleaned_data['search']
        return None

    def dispatch(self, request, *args, **kwargs):
        self.search_form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(name__icontains=self.search_value) | Q(description__icontains=self.search_value))
        return queryset

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.get_search_form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/detail_project.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()

        context['tasks'] = project.task_set.all()
        return context

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'projects/create_project.html'
    form_class = ProjectForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        form.instance.users.add(self.request.user)
        return response


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'projects/project_update.html'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('webapp:home')

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/project_delete.html'

    def get_success_url(self):
        return reverse('webapp:home')


class UpdateUserView(UpdateView):
    model = Project
    form_class = ProjectUserForm
    template_name = 'update_user.html'
    context_object_name = 'project'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('webapp:detail_project', kwargs={'pk': self.object.pk})


