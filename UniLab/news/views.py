from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import News, CategoryNews, TagNews
# Create your views here.
class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'

class NewsDetailView(DetailView):
    model = News

class CategoryDetailView(DetailView):
    model = CategoryNews
    
class TagDetailView(DetailView):
    model = TagNews