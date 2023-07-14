from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone #Imporza libreria de fechas
from django.contrib.auth.models import User #importar usuarios creados con el panel de admin

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = RichTextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de Publicación", default=timezone.now)
    imagePage = models.ImageField(verbose_name="Imagen", upload_to="images", null=True, blank=True)
    created = models.DateTimeField(verbose_name="Fecha de Creación", auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['-created']

    def __str__(self):
        return self.title