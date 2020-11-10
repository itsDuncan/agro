from django.urls import re_path
from .import views

app_name = 'dashboard'

urlpatterns = [
	re_path(r'^$', views.dashboard, name='dashboard'),
	re_path(r'^offer-advice/$', views.create_advice, name='offer-advice'),
	re_path(r'^advice/$', views.advice_list, name='advice-list'),
	re_path(r'^services/$', views.service_list, name='service-list'),
]