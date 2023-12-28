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

    def obtener_precio_ethereum(self):
        url_api_ethereum = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
        try:
            response = requests.get(url_api_ethereum)
            response.raise_for_status()
            data = response.json()
            precio_ethereum_usd = data["ethereum"]["usd"]
            return precio_ethereum_usd
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener el precio del Ethereum: {e}")
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        precio_bitcoin = self.obtener_precio_bitcoin()
        precio_ethereum = self.obtener_precio_ethereum()

        if precio_bitcoin is not None:
            precio_bitcoin = round(float(precio_bitcoin), 2)

        if precio_ethereum is not None:
            precio_ethereum = round(float(precio_ethereum), 2)

        # División del precio del dólar por el precio del bitcoin
        if self.object.dollarPrice is not None and precio_bitcoin != 0:
            context['precio_bitcoin'] = round(float(self.object.dollarPrice) / precio_bitcoin, 8)
        else:
            context['precio_bitcoin'] = None

        # División del precio del dólar por el precio del ethereum
        if self.object.dollarPrice is not None and precio_ethereum != 0:
            context['precio_ethereum'] = round(float(self.object.dollarPrice) / precio_ethereum, 8)
        else:
            context['precio_ethereum'] = None

        return context
