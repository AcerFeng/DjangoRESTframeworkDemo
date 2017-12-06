from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
    """
    列出所有代码片段（snippets），或者新建一个代码片段（snippet）
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    读取, 更新 或 删除 一个代码片段实例（snippet instance）。
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
