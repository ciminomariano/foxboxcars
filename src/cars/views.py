from django.views.generic import ListView, FormView
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.forms import formset_factory, modelformset_factory
from django.db import IntegrityError
from .forms import CarForm
from .models import Car


class CarCreateView(CreateView):
    model = Car
    template_name = 'cars/car_create.html'
    form_class = CarForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        CarFormSet = formset_factory(self.form_class, extra=1)
        formset = CarFormSet()
        context['formset'] = formset
        return context

    def form_valid(self, form):
        CarFormSet = formset_factory(self.form_class, extra=1)
        formset = CarFormSet(self.request.POST)
        if formset.is_valid():
            for form in formset:
                form.save()
            return redirect('car_list')
        return render(self.request, self.template_name, {'formset': formset})

    def post(self, request, *args, **kwargs):
        CarFormSet = formset_factory(self.form_class, extra=1)
        formset = CarFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                form.save()
            return redirect('car_list')
        return render(request, self.template_name, {'formset': formset})


class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'
    context_object_name = 'car_list'


class CarUpdateView(FormView):
    template_name = 'cars/car_update.html'
    form_class = CarForm
    success_url = '/car_list/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car_list = Car.objects.all()
        CarFormSet = modelformset_factory(Car, form=self.form_class, extra=0)
        formset = CarFormSet(initial=[
            {'id': car.id, 'brand': car.brand, 'model': car.model, 'main_color': car.main_color, 'value': car.value,
             'production_costs': car.production_costs, 'transportation_costs': car.transportation_costs} for car in
            car_list])
        context['formset'] = formset
        return context

    def form_valid(self, form):
        CarFormSet = formset_factory(self.form_class, extra=1)
        formset = CarFormSet(self.request.POST)
        if formset.is_valid():
            for form in formset:
                form.save()
            return redirect('car_list')
        return render(self.request, self.template_name, {'formset': formset})

    def post(self, request, *args, **kwargs):


        CarFormSet = formset_factory(self.form_class, extra=1)
        formset = CarFormSet(request.POST)

        if formset.is_valid():
            try:
                Car.objects.all().delete()
            except Exception as e:
                error_message = "Error occurred while deleting cars: " + str(e)
                return render(request, self.template_name, {'error_message': error_message})

            instances = []

            for form in formset:
                instance = form.save(commit=False)
                instances.append(instance)

            try:
                Car.objects.bulk_create(instances)
                return redirect('car_list')

            except IntegrityError as e:
                error_message = "Error occurred while saving cars: " + str(e)
                return render(request, self.template_name, {'formset': formset, 'error_message': error_message})

            except Exception as e:
                error_message = "Error occurred while saving cars: " + str(e)
                return render(request, self.template_name, {'formset': formset, 'error_message': error_message})

        return render(request, self.template_name, {'formset': formset})

