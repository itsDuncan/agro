from django.shortcuts import render
from .forms import AdviceForm

def dashboard(request):
	template_name = 'dashboard/dashboard.html'

	context = {

	}
	return render(request, template_name, context)

def create_advice(request):
	template_name = 'dashboard/create_advice.html'
	form = AdviceForm(request.POST or None, label_suffix='')
	
	context = {
		'form': form,
	}
	return render(request, template_name, context)