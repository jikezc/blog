from django.shortcuts import render
from .models import ArticlePost, ArticleCategroy, Messages
from .serializers import ArticleCategroyModelSerializer, ArticlePostModelSerializer, ArticleRetrieveModelSerializer, \
    MessagesModelSerializer, GiveLikeModelSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .paginations import CustomPageNumberPagination

import logging

log = logging.getLogger("django")


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
    # 指定分页器
    pagination_class = CustomPageNumberPagination


class ArticleRetrieveAPIView(RetrieveAPIView):
    """
    文章详情视图类
    """
    queryset = ArticlePost.objects.filter(is_show=True, is_delete=False)
    serializer_class = ArticleRetrieveModelSerializer

    def get(self, request, *args, **kwargs):
        super().get(self, request, *args, **kwargs)
        try:
            id = kwargs.get("pk")
            add_view_obj = ArticlePost.objects.get(id=id, is_show=True, is_delete=False)
            add_view_obj.views_count += 1
            add_view_obj.save(update_fields=['views_count'])
        except:
            log.error("文章浏览量增加失败")
        return self.retrieve(request, *args, **kwargs)


class MessagesListAPIView(ListAPIView):
    """留言板视图类"""
    queryset = Messages.objects.all()
    serializer_class = MessagesModelSerializer


class MessagesCreateAPIView(CreateAPIView):
    """留言板新增留言视图类"""
    queryset = Messages.objects.all()
    serializer_class = MessagesModelSerializer


class HomeArticleListAPIView(ListAPIView):
    """
    文章视图类
    """
    queryset = ArticlePost.objects.filter(is_show=True, is_delete=False).order_by('-sort')[0:3]
    serializer_class = ArticlePostModelSerializer


class GiveLikeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """点赞视图类"""
    queryset = ArticlePost.objects.filter(is_show=True, is_delete=False)
    serializer_class = GiveLikeModelSerializer
