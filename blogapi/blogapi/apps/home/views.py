from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Slideshow
from .serializers import SlideshowModelSerializer
from django.db.models import Q


# Create your views here.
class SlideshowListAPIView(ListAPIView):
    """
    轮播图的类视图
    """
    queryset = Slideshow.objects.filter(Q(is_show=True) & Q(is_delete=False)).order_by("sort")
    serializer_class = SlideshowModelSerializer