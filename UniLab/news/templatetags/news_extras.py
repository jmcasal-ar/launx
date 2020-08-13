from django import template
from news.models import News, CategoryNews, TagNews

#Registramos el archivo como template
register = template.Library()

#Creamos metodo para obtener todas las paginas. El @ es un decorador para registrar nuestra funcion como simple tag
@register.simple_tag
def get_news_list():
    news = News.objects.all()
    return news

@register.simple_tag
def get_categories_list():
    categories = CategoryNews.objects.all()
    return categories

@register.simple_tag
def get_tags_list():
    tags = TagNews.objects.all()
    return tags