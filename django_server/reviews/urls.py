from django.urls import path, include

from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('c/all', views.all_companies, name='all_companies'),
	path('c/<str:name>', views.company_details, name='company_details'),
]
