from django.contrib import admin
from .models import News, CategoryNews, TagNews

# Register your models here.
class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    #Visualizamos columnas en el panel. El __ se usa para campos relacionales
    list_display = ('title', 'published')
    #ordenamos el panel
    ordering = ('published', 'title' ) 
    #agregamos una caja de busqueda por los siguientes campos
    search_fields = ('title','categories_name')
    #agregamos un panel de visualización por jerarquia
    date_hierarchy = 'published'



admin.site.register(TagNews, TagAdmin)
admin.site.register(CategoryNews, CategoryAdmin)
admin.site.register(News, NewsAdmin)
