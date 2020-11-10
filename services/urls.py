from django.urls import re_path
from .import views

app_name = 'services'

urlpatterns = [
	re_path(r'^$', views.create_service, name='create-service'),
]