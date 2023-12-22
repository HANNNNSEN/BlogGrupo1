from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Post, Categoria
import os


class PostListView(ListView):
    model=Post
    template_name='blog/posteos/post_list.html'
    context_object_name='posteos'

class PostDetailView(DetailView):
    model=Post
    template_name='blog/posteos/post_view.html'
    context_object_name='post'

class PostCreateView(CreateView):
    model=Post
    template_name='blog/posteos/post_create.html'
    context_object_name='post'
    fields='__all__'
    success_url=reverse_lazy('post_list')

class PostUpdateView(UpdateView):
    model=Post
    template_name='blog/posteos/post_create.html'
    context_object_name='post'
    fields='__all__'
    success_url=reverse_lazy('post_list')


class PostDeleteView(DeleteView):
    model=Post
    template_name='blog/posteos/post_confirm_delete.html'
    context_object_name='post'
    success_url=reverse_lazy('post_list')
    #la función delete la utilizaremos cuando se borre un post borre las imagenes para no saturar el servidor
    def form_valid(self, form):
        #devuelve el objeto post
        post=self.get_object()
        # se copia la ruta en una variable
        if post.imagen:
            imagen_path= post.imagen.path
        # se pregunta si existe esa ruta
            if os.path.exists(imagen_path):
                os.remove(imagen_path)
        return super().form_valid(form)
    
class CategoriaListView(ListView):
    model=Categoria
    template_name='blog/categorias/categoria_list.html'
    context_object_name='categorias'

class CategoriaDetailView(DetailView):
    model=Categoria
    template_name='blog/categorias/categoria_view.html'
    context_object_name='categoria'

class CategoriaCreateView(CreateView):
    model=Categoria
    template_name='blog/categorias/categoria_create.html'
    context_object_name='categoria'
    fields='__all__'
    success_url=reverse_lazy('categoria_list')

class CategoriaUpdateView(UpdateView):
    model=Categoria
    template_name='blog/categorias/categoria_create.html'
    context_object_name='categoria'
    fields='__all__'
    success_url=reverse_lazy('categoria_list')


class CategoriaDeleteView(DeleteView):
    model=Categoria
    template_name='blog/categorias/categoria_confirm_delete.html'
    context_object_name='categoria'
    success_url=reverse_lazy('categoria_list')
    #la función delete la utilizaremos cuando se borre un post borre las imagenes para no saturar el servidor
    def form_valid(self, form):
        #devuelve el objeto post
        post=self.get_object()
        # se copia la ruta en una variable
        if post.imagen:
            imagen_path= post.imagen.path
        # se pregunta si existe esa ruta
            if os.path.exists(imagen_path):
                os.remove(imagen_path)
        return super().form_valid(form)