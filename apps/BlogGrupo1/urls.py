from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView, PostDeleteView,PostUpdateView,CategoriaCreateView,CategoriaDeleteView,CategoriaDetailView,CategoriaListView,CategoriaUpdateView


urlpatterns = [
    path(
        route='Post/List/',
        view=PostListView.as_view(), 
        name='post_list'),
    path(
        route='Post/<int:pk>',
        view=PostDetailView.as_view(), 
        name='post_view'),
    path(
        route='Post/Create/',
        view=PostCreateView.as_view(), 
        name='post_create'),
    path(
        route='Post/<int:pk>/Update/',
        view=PostUpdateView.as_view(), 
        name='categoria_update'),
    path(
        route='Post/<int:pk>/Delete/',
        view=PostDeleteView.as_view(), 
        name='post_confirm_delete'),
    path(
        route='Categoria/List/',
        view=CategoriaListView.as_view(), 
        name='categoria_list'),
    path(
        route='Categoria/<int:pk>',
        view=CategoriaDetailView.as_view(), 
        name='categoria_view'),
    path(
        route='Categoria/Create/',
        view=CategoriaCreateView.as_view(), 
        name='categoria_create'),
    path(
        route='Categoria<int:pk>/Update/',
        view=CategoriaUpdateView.as_view(), 
        name='categoria_update'),
    path(
        route='Categoria/<int:pk>/Delete/',
        view=CategoriaDeleteView.as_view(), 
        name='categoria_confirm_delete'),
]
