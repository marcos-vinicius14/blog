"""
Configuração de URLs para a API do projeto.

Este módulo utiliza o DefaultRouter do Django REST Framework para registrar
os ViewSets e gerar automaticamente as rotas RESTful padrão (list, create,
retrieve, update, partial_update, destroy) para os seguintes recursos:
- Posts
- Categories
- Tags

As URLs geradas são incluídas na lista `urlpatterns` para serem
disponibilizadas pela aplicação Django.
"""


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CategoryViewSet, TagViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls))
]