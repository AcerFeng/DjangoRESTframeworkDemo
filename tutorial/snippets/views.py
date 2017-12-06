from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from snippets.serializers import UserSerializer
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User
from snippets.permissions import IsOwnerOrReadOnly


class SnippetList(generics.ListCreateAPIView):
    """
    列出所有代码片段（snippets），或者新建一个代码片段（snippet）
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    读取, 更新 或 删除 一个代码片段实例（snippet instance）。
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer