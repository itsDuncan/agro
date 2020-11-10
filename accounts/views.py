from django.shortcuts import render, get_object_or_404
from .models import User
from .forms import ProfileUpdateForm

def profile_list(request):
	template_name = 'accounts/profile_list.html'
	farmers = User.objects.all().exclude(username='admin')

	context = {
		'farmers': farmers,
	}

	return render(request, template_name, context)

def profile_detail(request, username):
	template_name = 'accounts/profile_detail.html'
	profile = get_object_or_404(User, username=request.user.username)

	form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=profile)

	if form.is_valid():
		form.save()
		messages.success(request, "Profile Updated!")

	context = {
		'profile': profile,
		'form': form,
	}

	return render(request, template_name, context)