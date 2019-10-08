from django.shortcuts import render
from .models import ArticlePost, ArticleCategroy, Messages
from .serializers import ArticleCategroyModelSerializer, ArticlePostModelSerializer, ArticleRetrieveModelSerializer, \
    MessagesModelSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class ArticleCategroyListAPIView(ListAPIView):
    """
    文章分类视图类
    """
    queryset = ArticleCategroy.objects.filter(is_show=True, is_delete=False).order_by('sort')
    serializer_class = ArticleCategroyModelSerializer


class ArticlePostListAPIView(ListAPIView):
    """
    文章视图类
    """
    queryset = ArticlePost.objects.filter(is_show=True, is_delete=False).order_by('sort')
    serializer_class = ArticlePostModelSerializer
    # 文章分类配置
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ('article_categroy',)


class ArticleRetrieveAPIView(RetrieveAPIView):
    """
    文章详情视图类
    """
    queryset = ArticlePost.objects.filter(is_show=True, is_delete=False)
    serializer_class = ArticleRetrieveModelSerializer


class MessagesListAPIView(ListAPIView):
    """留言板视图类"""
    queryset = Messages.objects.all()
    serializer_class = MessagesModelSerializer


class MessagesCreateAPIView(CreateAPIView):
    """留言板新增留言视图类"""
    queryset = Messages.objects.all()
    serializer_class = MessagesModelSerializer