from rest_framework.serializers import ModelSerializer
from .models import Slideshow


class SlideshowModelSerializer(ModelSerializer):
    """
    轮播图序列化器
    """
    class Meta:
        model = Slideshow
        fields = ('image', 'link')