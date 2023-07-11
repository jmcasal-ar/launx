from django.urls import path
from .views import CourseListView, CourseDetailView, PaymentDetailView


courses_patterns = ([
    path('', CourseListView.as_view(), name='courses'),
    path('<int:pk>/<slug:slug>/', CourseDetailView.as_view(), name='course'),
    path('payment/<int:pk>/<slug:slug>/', PaymentDetailView.as_view(), name='payment'),
], "courses")