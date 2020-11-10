from django.shortcuts import render
from .forms import CreateServiceForm

def create_service(request):
	template_name = 'dashboard/create_service.html'
	form = CreateServiceForm(request.POST or None, label_suffix='')

	context = {
		'form': form,
	}

	return render(request, template_name, context)