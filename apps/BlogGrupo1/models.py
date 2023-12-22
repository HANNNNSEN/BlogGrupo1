from django.db import models
from django.utils import timezone



class Categoria(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    imagen = models.ImageField(upload_to='media', default='static/categoria/post_default.png')
    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return f'nombre: {self.nombre}'


class Post(models.Model):
    titulo = models.CharField(max_length=255, unique=True, null=False)
    #user = models.ForeignKey(User, on_delete=models.PROTECT)
    #perfil = models.ForeignKey(Perfil, on_delete=models.PROTECT)
    subtitulo = models.CharField(max_length=255, unique=True,null=True, blank=True)
    #url = models.SlugField(max_length=255, unique=True)
    #resumen = RichTextField() --> este es para usar el ckeditor
    #contenido = RichTextField() --> este es para usar el ckeditor 
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)
    contenido=models.TextField(null=False)
    visible = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='Sin Categoria')
    imagen = models.ImageField(upload_to='media', default='static/post/post_default.png')
    vistas = models.PositiveIntegerField(default=0)
    destacado = models.BooleanField(default=False)
     

    class Meta:
        ordering = ('fecha_creado',)
        
    def __str__(self):
        return f'categoria: {self.categoria} - titulo: {self.titulo} - subtitulo: {self.subtitulo} imagen: {self.imagen}' #- {self.user.username}'
    
