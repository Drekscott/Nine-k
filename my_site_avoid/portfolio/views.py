from django.shortcuts import render
from .models import PortfolioCreation
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from my_site_avoid.models import User
# Create your views here.

class PortfolioCreationView(DetailView):
    model = PortfolioCreation

    def get_context_data(self, **kwargs):
        context = super(PortfolioCreationView, self).get_context_data(**kwargs)
        return context
