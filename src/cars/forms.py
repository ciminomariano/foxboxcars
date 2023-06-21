from django import forms
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'main_color', 'value', 'production_costs', 'transportation_costs']


    def clean_value(self):
        value = self.cleaned_data['value']
        if value <= 0:
            raise forms.ValidationError("Value must be a positive number.")
        return value

    def clean_production_costs(self):
        production_costs = self.cleaned_data['production_costs']
        if production_costs <= 0:
            raise forms.ValidationError("Production Costs must be a positive number.")
        return production_costs

    def clean_transportation_costs(self):
        transportation_costs = self.cleaned_data['transportation_costs']
        if transportation_costs <= 0:
            raise forms.ValidationError("Transportation Costs must be a positive number.")
        return transportation_costs
