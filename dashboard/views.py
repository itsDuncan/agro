from django.shortcuts import render

def dashboard(request):
	template_name = 'dashboard/dashboard.html'

	context = {

	}
	return render(request, template_name, context)