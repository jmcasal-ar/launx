from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Course

# Create your views here.
class CourseListView(ListView):
    model = Course
    template_name = 'courses/courses_list.html'

class CourseDetailView(DetailView):
    model = Course

class PaymentDetailView(DetailView):
    model = Course
    template_name = 'courses/payment_detail.html'