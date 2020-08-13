from django.urls import path
from .views import CourseListView, CourseDetailView


courses_patterns = ([
    path('', CourseListView.as_view(), name='courses'),
    path('<int:pk>/<slug:slug>/', CourseDetailView.as_view(), name='course'),
], "courses")