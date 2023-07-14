from django.contrib import admin
from .models import Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    #Visualizamos columnas en el panel. El __ se usa para campos relacionales
    list_display = ('title', 'published')
    #ordenamos el panel
    ordering = ('published', 'title' ) 
    #agregamos un panel de visualización por jerarquia
    date_hierarchy = 'published'

admin.site.register(Page, PageAdmin)
