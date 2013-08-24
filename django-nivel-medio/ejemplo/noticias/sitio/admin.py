from django.contrib import admin
from sitio.models import Noticia, Comentario, Categoria

class AdminNoticia(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha', 'archivada')
    list_filter = ('archivada', 'fecha')
    search_fields = ('texto', 'titulo')
    date_hierarchy = 'fecha'

admin.site.register(Noticia, AdminNoticia)
admin.site.register(Categoria)
admin.site.register(Comentario)


