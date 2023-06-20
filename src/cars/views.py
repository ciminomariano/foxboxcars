from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.forms import formset_factory
from django.shortcuts import render, redirect
from .forms import CarForm
from .models import Car


def car_create(request):
    CarFormSet = formset_factory(CarForm, extra=1)

    if request.method == 'POST':
        formset = CarFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                form.save()
            return redirect('car_list')
    else:
        formset = CarFormSet()

    return render(request, 'cars/car_create.html', {'formset': formset})


class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'  # Ruta a tu plantilla
    context_object_name = 'car_list'  # Nombre del objeto de contexto en la plantilla


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car_update.html'
    success_url = '/'
