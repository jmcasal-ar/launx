from django.urls import path
from .views import PageDetailView

pages_patterns = ([
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='pages'),
], "pages")