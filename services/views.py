from django.shortcuts import render
from .forms import CreateServiceForm
from .models import Service

def create_service(request):
	template_name = 'dashboard/create_service.html'
	if request.method == 'POST':
		form = CreateServiceForm(request.POST or None, label_suffix='')
		if form.is_valid():
			form.save()
	else:
		form = CreateServiceForm(label_suffix='')

	context = {
		'form': form,
	}

	return render(request, template_name, context)