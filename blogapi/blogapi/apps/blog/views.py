from django.shortcuts import render
from .models import ArticlePost, ArticleCategroy
from .serializers import ArticleCategroyModelSerializer, ArticlePostModelSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class ArticleCategroyListAPIView(ListAPIView):
    """
    文章分类序列化器类
    """
    queryset = ArticleCategroy.objects.filter(is_show=True, is_delete=False).order_by('sort')
    serializer_class = ArticleCategroyModelSerializer


class AriclePostListAPIView(ListAPIView):
    """
    文章序列化器类
    """
    queryset = ArticlePost.objects.filter(is_show=True, is_delete=False).order_by('sort')
    serializer_class = ArticlePostModelSerializer
    # 文章分类配置
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ('article_categroy',)
