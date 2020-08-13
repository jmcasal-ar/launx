from django.contrib import admin
from .models import Course, University, Tag, Category, Professor, ModalityCourse

# Register your models here.
class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ModalityCourseAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    #Visualizamos columnas en el panel. El __ se usa para campos relacionales
    list_display = ('title', 'published')
    #ordenamos el panel
    ordering = ('professor', 'published' ) 
    #agregamos una caja de busqueda por los siguientes campos
    search_fields = ('title', 'program', 'author_usernmane', 'categories_name')
    #agregamos un panel de visualización por jerarquia
    date_hierarchy = 'published'


class ProfessorAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class UniversityAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(ModalityCourse, ModalityCourseAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(University, UniversityAdmin)

