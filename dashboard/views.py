from django.shortcuts import render
from .forms import AdviceForm
from .models import Advice
from services.models import Service

def dashboard(request):
	template_name = 'dashboard/dashboard.html'

	context = {

	}
	return render(request, template_name, context)

def create_advice(request):
	template_name = 'dashboard/create_advice.html'

	if request.method == 'POST':
		form = AdviceForm(request.POST or None, label_suffix='')
		if form.is_valid():
			form.save()
	else:
		form = AdviceForm(label_suffix='')
	
	context = {
		'form': form,
	}
	return render(request, template_name, context)

def advice_list(request):
	template_name = 'dashboard/advice_list.html'
	advice_list = Advice.objects.all()

	context = {
		'advice_list': advice_list,
	}
	return render(request, template_name, context)

def service_list(request):
	template_name = 'dashboard/service_list.html'
	services = Service.objects.all()

	context = {
		'services': services,
	}
	return render(request, template_name, context)