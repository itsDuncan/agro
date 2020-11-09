from django.shortcuts import render

def home(request):
	template_name = 'landing_page/main.html'
	context = {

	}
	return render(request, template_name, context)