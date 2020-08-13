from django import template
from courses.models import Course

#Registramos el archivo como template
register = template.Library()

#Creamos metodo para obtener todas las paginas. El @ es un decorador para registrar nuestra funcion como simple tag
@register.simple_tag
def get_courses_list():
    courses = Course.objects.all()
    return courses