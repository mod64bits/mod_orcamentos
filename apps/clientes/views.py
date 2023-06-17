from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from .models import Cliente


class ClienteListeView(ListView):
    model = Cliente
    paginate_by = 100
    template_name = ''


class ClienteCreateView(CreateView):
    model = Cliente
    fields = '__all__'
    template_name = ''


class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = '__all__'
    template_name = ''


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = ''
