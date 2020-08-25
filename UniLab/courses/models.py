from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import now #Imporza libreria de fechas

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ['-created']

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"
        ordering = ['-created']

    def __str__(self):
        return self.name

class ModalityCourse(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")

    class Meta:
        verbose_name = "modalidad de cursada"
        verbose_name_plural = "modalidades de cursada"
        ordering = ['-created']

    def __str__(self):
        return self.name

class University(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    acronym = models.CharField(max_length=20, verbose_name="Acrónimo", blank=True, null=True)
    logo = models.ImageField(upload_to="university", verbose_name="Logo", null=True, blank=True)
    country = models.CharField(max_length=100, verbose_name="País")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")

    class Meta:
        verbose_name = "universidad"
        verbose_name_plural = "universidades"
        ordering = ['-created']

    def __str__(self):
        return self.name

class Professor(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre y Apellido")
    profession = models.CharField(verbose_name="Profesión", max_length=300, blank=True, null=True)
    photo = models.ImageField(upload_to="professor", verbose_name="Foto", null=True, blank=True)
    bio = RichTextField(verbose_name="Biografia", blank=True, null=True)
    dni = models.IntegerField(verbose_name="DNI", blank=True, null=True)
    email = models.EmailField(verbose_name="Correo electrónico", blank=True, null=True)
    cellPhone = models.TextField(verbose_name="Celular", blank="True", null=True)
    linkedin = models.URLField(verbose_name="Linkedin", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")


    class Meta:
        verbose_name = "profesor"
        verbose_name_plural = "profesores"
        ordering = ['-created']

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    professor = models.ManyToManyField(Professor, verbose_name="Profesor", related_name="get_professors")
    objective = RichTextField(verbose_name="Objetivo", blank=True, null=True)
    program = RichTextField(verbose_name="Programa", blank=True, null=True)
    imageCourse = models.ImageField(upload_to="imageCourses", verbose_name="Imagen del Curso", null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    dollarPrice = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio en dolares", blank=True, null=True)
    pesoPrice = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio en pesos", blank=True, null=True)
    modality = models.ManyToManyField(ModalityCourse, verbose_name="Modalidad", related_name="get_modalities")
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_categories")
    tags = models.ManyToManyField(Tag, verbose_name="Tags", related_name="get_tags")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    published = models.DateTimeField(verbose_name="Fecha de Publicación", default=now())
    university = models.ManyToManyField(University, verbose_name="Universidad", related_name="get_course_universitys")
    hoursDuration = models.SmallIntegerField(verbose_name="Horas de Duración del curso", blank=True, null=True)
    urlMercadoPago = models.URLField(max_length=200, null=True, blank=True)
    urlPayPaL = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title