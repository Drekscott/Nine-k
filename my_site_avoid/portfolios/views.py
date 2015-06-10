from django.shortcuts import render
from .models import PortfolioCreation
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
# Create your views here.

class PortfolioCreationView(DetailView):
    
    model = PortfolioCreation
    template_name = 'portfolio_creation.html'
