"""
Configuração de URLs principal do projeto Django.

Este arquivo é o ponto de entrada para o roteamento de todas as URLs do projeto.
Ele mapeia os caminhos de URL de nível superior para as aplicações ou
funcionalidades correspondentes.

As rotas definidas aqui incluem:
- '/admin/': Para o painel de administração do Django.
- '/api/': Para todos os endpoints da API, que são gerenciados pela
"""

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog_api.urls'))
]
