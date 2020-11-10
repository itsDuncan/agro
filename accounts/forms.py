from django import forms
from .models import User

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'firstname', 'lastname', 'email', 'phone_number', 'description', 'wholesaler']

	def __init__(self, *args, **kwargs):
		super(ProfileUpdateForm, self).__init__(*args, **kwargs)
		for fieldname, field in self.fields.items():
			field.widget.attrs.update({
				'class': 'form-control',
			})