from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from decimal import Decimal  # Añade esta línea al inicio de tu archivo
from django.core.cache import cache
from datetime import datetime, timedelta
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
            precio_bitcoin_usd = data.get("bitcoin", {}).get("usd")
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
            precio_ethereum_usd = data.get("ethereum", {}).get("usd")
            return precio_ethereum_usd
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener el precio del Ethereum: {e}")
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Claves para la caché
        btc_cache_key = 'btc_price'
        eth_cache_key = 'eth_price'

        # Obtener precios almacenados en caché
        precio_bitcoin = cache.get(btc_cache_key)
        precio_ethereum = cache.get(eth_cache_key)

        # Verificar si los precios están almacenados en caché y si han pasado 24 horas
        if precio_bitcoin is None or precio_ethereum is None or \
                cache.get('last_update_time') is None or \
                (datetime.now() - cache.get('last_update_time')).days >= 1:

            try:
                # Obtener los precios actualizados
                precio_bitcoin = self.obtener_precio_bitcoin()
                precio_ethereum = self.obtener_precio_ethereum()

                # Guardar precios en caché
                cache.set(btc_cache_key, precio_bitcoin)
                cache.set(eth_cache_key, precio_ethereum)

                # Actualizar el tiempo de la última actualización
                cache.set('last_update_time', datetime.now())
            except Exception as e:
                print(f"Error al actualizar la caché: {e}")

        if precio_bitcoin is not None:
            precio_bitcoin = round(float(precio_bitcoin), 2)

        if precio_ethereum is not None:
            precio_ethereum = round(float(precio_ethereum), 2)

        if self.object.dollarPrice is not None and precio_bitcoin is not None and precio_bitcoin != 0:
            context['precio_bitcoin'] = round(Decimal(self.object.dollarPrice) / Decimal(precio_bitcoin), 8)
        else:
            context['precio_bitcoin'] = None

        if self.object.dollarPrice is not None and precio_ethereum is not None and precio_ethereum != 0:
            context['precio_ethereum'] = round(Decimal(self.object.dollarPrice) / Decimal(precio_ethereum), 8)
        else:
            context['precio_ethereum'] = None

        print(f"self.object.dollarPrice: {self.object.dollarPrice}")
        print(f"precio_bitcoin: {precio_bitcoin}")

        return context