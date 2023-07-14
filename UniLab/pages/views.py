from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Page

# Create your views here.
class PageDetailView(DetailView):
    model = Page