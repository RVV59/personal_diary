from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Entry

class EntryListView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'diary/entry_list.html'
    context_object_name = 'entries'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().filter(author=self.request.user)
        query = self.request.GET.get('q', '')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
        return queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context

class EntryDetailView(LoginRequiredMixin, DetailView):
    model = Entry
    template_name = 'diary/entry_detail.html'
    context_object_name = 'entry'

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = 'diary/entry_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('diary:entry_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EntryUpdateView(LoginRequiredMixin, UpdateView):
    model = Entry
    template_name = 'diary/entry_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('diary:entry_list')

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

class EntryDeleteView(LoginRequiredMixin, DeleteView):
    model = Entry
    template_name = 'diary/entry_confirm_delete.html'
    success_url = reverse_lazy('diary:entry_list')

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
