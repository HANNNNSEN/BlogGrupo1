from django.contrib import admin
from .models import Categoria, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('id','titulo','subtitulo','fecha_creado','fecha_modificado','contenido','vistas','categoria','imagen','visible','destacado')

@admin.register(Categoria)
class PostAdmin(admin.ModelAdmin):
    list_display=('id','nombre','imagen')

# Register your models here.
