from rest_framework import viewsets, permissions
from .serializers import PostSerializer, TagSerializer, CategorySerializer
from .models import Post, Tag, Category


class PostViewSet(viewsets.ModelViewSet):
    """
     ViewSet para Posts com permissões dinâmicas:
    - Apenas Admins podem criar novos posts.
    - Leitura é pública.
    - Apenas usuários autenticados podem editar ou deletar.
    """

    queryset = Post.objects.all().select_related('author', 'category').prefetch_related('tags')
    serializer_class = PostSerializer

    def get_permissions(self):
        """
        Instancia e retorna a lista de permissões que esta view requer,
        baseado na ação (request method).
        """
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]

        if self.action == 'create':
            permission_classes = [permissions.IsAdminUser]

        return [permission() for permission in permission_classes]


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]