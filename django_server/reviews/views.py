from django.shortcuts import render

from .models import Company, Review

def home(request):
	return render(request, 'reviews/home.html')

# def about(request):
# 	return render(request, 'about.html')

# def contact(request):
# 	return render(request, 'contact.html')

def all_companies(request):
	companies = Company.objects.all()
	return render(request, 'reviews/all_companies.html', {'companies': companies})

def company_details(request, name):
	company = Company.objects.get(name=name)
	reviews = Review.objects.filter(company=company)
	return render(request, 'reviews/company_details.html', {'company': company, 'reviews': reviews})
