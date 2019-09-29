from django.shortcuts import render
from .models import ArticlePost, ArticleCategroy
from .serializers import ArticleCategroyModelSerializer
from rest_framework.generics import ListAPIView


# Create your views here.
class ArticleCategroyListAPIView(ListAPIView):
    queryset = ArticleCategroy.objects.filter(is_show=True, is_delete=False).order_by('sort')
    serializer_class = ArticleCategroyModelSerializer