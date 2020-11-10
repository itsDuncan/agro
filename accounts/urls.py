from django.urls import re_path
from .import views

app_name = 'profile'

urlpatterns = [
	re_path(r'^$', views.profile_list, name='profile-list'),
	re_path(r'^detail/(?P<username>[\w-]+)/$', views.profile_detail, name='profile-detail'),
]