from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import Car
from .forms import CarForm


class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'  # Ruta a tu plantilla
    context_object_name = 'car_list'  # Nombre del objeto de contexto en la plantilla


class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car_create.html'
    success_url = '/'


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car_update.html'
    success_url = '/'