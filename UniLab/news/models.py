from django.db import models
from django.utils import timezone #Imporza libreria de fechas
from django.contrib.auth.models import User #importar usuarios creados con el panel de admin
from ckeditor.fields import RichTextField

class CategoryNews(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ['-created']

    def __str__(self):
        return self.name

class TagNews(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"
        ordering = ['-created']

    def __str__(self):
        return self.name

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = RichTextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de Publicación", default=timezone.now)
    imageNews = models.ImageField(verbose_name="Imagen", upload_to="news", null=True, blank=True)
    #Enlazar con Foreign Key en cascada
    authorNews = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categoriesNews = models.ManyToManyField(CategoryNews, verbose_name="Categorias", related_name="get_categories")
    tagsNews = models.ManyToManyField(TagNews, verbose_name="Tags", related_name="get_tags")
    created = models.DateTimeField(verbose_name="Fecha de Creación", auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")

    class Meta:
        verbose_name = "noticia"
        verbose_name_plural = "noticias"
        ordering = ['-created']

    def __str__(self):
        return self.title