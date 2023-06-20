from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.forms import formset_factory
from .forms import CarForm
from .models import Car


class CarCreateView(ListView):
    model = Car
    template_name = 'cars/car_create.html'  # Ruta a tu plantilla
    context_object_name = 'car_list'  # Nombre del objeto de contexto en la plantilla

    def get(self, request, *args, **kwargs):
        CarFormSet = formset_factory(CarForm, extra=1)
        formset = CarFormSet()
        return render(request, self.template_name, {'formset': formset})

    def post(self, request, *args, **kwargs):
        CarFormSet = formset_factory(CarForm, extra=1)
        formset = CarFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                form.save()
            return redirect('car_list')
        return render(request, self.template_name, {'formset': formset})


class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'  # Ruta a tu plantilla
    context_object_name = 'car_list'  # Nombre del objeto de contexto en la plantilla


class CarUpdateView(FormView):
    template_name = 'cars/car_update.html'
    form_class = CarForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car_list'] = Car.objects.all()
        return context

    def form_valid(self, form):
        for car in form.cleaned_data:
            car_instance = Car.objects.get(id=car.id)
            car_instance.production_costs = car.production_costs
            car_instance.transportation_costs = car.transportation_costs
            car_instance.total = car.production_costs + car.transportation_costs
            car_instance.save()
        return super().form_valid(form)
