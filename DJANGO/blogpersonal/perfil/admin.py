from django.contrib import admin

# Models
from .models import Project


# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    admin.site.site_header = ' '  # Establece el encabezado del sitio en una cadena vacía
    admin.site.index_title = ' '  # Establece el título de la página de inicio en una cadena vacía
    admin.site.site_title = ' '  # Establece el título de la pestaña del navegador en una cadena vacía

    list_display = ('id', 'title', 'desc', 'created',)
    list_editable = ('title', 'desc',)
    list_filter = ('title', 'created', 'updated',)
    search_fields = ('id','title', 'desc',)



#admin.site.register(Project)
