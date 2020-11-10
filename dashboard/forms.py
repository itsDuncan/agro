from django import forms
from .models import Advice

class AdviceForm(forms.ModelForm):
	class Meta:
		model = Advice
		fields = ['specialization', 'content']

	specialization = forms.CharField(
		required = True,
		label = 'Specialization',
		widget = forms.TextInput(
			attrs = {
				'class': 'form-control',
				'placeholder': 'Area of specialization'
			}),
	)

	content = forms.CharField(
		required = True,
		label = 'Message',
		widget = forms.Textarea(
			attrs = {
				'class': 'form-control mb-3',
				'placeholder': 'What can you tell us...',
				'rows': 5,
		}),
	)