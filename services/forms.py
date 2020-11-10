from django import forms
from .models import Service

class CreateServiceForm(forms.ModelForm):
	class Meta:
		model = Service
		fields = ['name', 'description', 'unit_of_measure']

	name = forms.CharField(
		required = True,
		label = 'Service Name',
		widget = forms.TextInput(
			attrs = {
				'class': 'form-control',
				'placeholder': 'What do you offer!'
			}),
	)

	description = forms.CharField(
		required = True,
		label = 'Description',
		widget = forms.Textarea(
			attrs = {
				'class': 'form-control mb-3',
				'placeholder': 'Kindly give a brief but detailed description about the service',
				'rows': 5,
		}),
	)

	unit_of_measure = forms.CharField(
		required = True,
		label = 'Unit of measure',
		widget = forms.TextInput(
			attrs = {
				'class': 'form-control',
				'placeholder': 'Package, Units e.t.c',
			}),
	)