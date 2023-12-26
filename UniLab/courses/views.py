from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Course
from django.shortcuts import render
import requests

# Create your views here.
class CourseListView(ListView):
    model = Course
    template_name = 'courses/courses_list.html'

class CourseDetailView(DetailView):
    model = Course

class PaymentDetailView(DetailView):
    model = Course
    template_name = 'courses/payment_detail.html'
    context_object_name = 'course'

    def obtener_precio_bitcoin(self):
        url_api_bitcoin = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        try:
            response = requests.get(url_api_bitcoin)
            response.raise_for_status()
            data = response.json()
            precio_bitcoin_usd = data["bitcoin"]["usd"]
            return precio_bitcoin_usd
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener el precio del Bitcoin: {e}")
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        precio_bitcoin = self.obtener_precio_bitcoin()

        if precio_bitcoin is not None:
            precio_bitcoin = round(precio_bitcoin, 2)

        context['precio_bitcoin'] = precio_bitcoin
        return context
