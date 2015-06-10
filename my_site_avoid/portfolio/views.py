from django.shortcuts import render
from .models import PortfolioCreation
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
# Create your views here.

class PortfolioCreationView(ListView):
    
    def get_portfolio(request):
        
        portfolio_creation_list = PortfolioCreation.objects.all()
        return HttpResponse(portfolio_creation_list)
