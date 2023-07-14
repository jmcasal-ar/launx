from django import template
from pages.models import Page

#Registramos el archivo como template
register = template.Library()

#Creamos metodo para obtener todas las paginas. El @ es un decorador para registrar nuestra funcion como simple tag
@register.simple_tag
def get_pages_list():
    pages = Page.objects.all()
    return pages
