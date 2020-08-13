from django.urls import path
from .views import NewsListView, NewsDetailView, CategoryDetailView, TagDetailView


news_patterns = ([
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:pk>/<slug:slug>/', NewsDetailView.as_view(), name='news'),
    path('category/<int:pk>/<slug:slug>/', CategoryDetailView.as_view(), name='categories'),
    path('tag/<int:pk>/<slug:slug>/', TagDetailView.as_view(), name='tags'),
], "news")