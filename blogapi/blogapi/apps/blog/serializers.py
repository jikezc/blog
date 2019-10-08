from rest_framework.serializers import ModelSerializer
from .models import ArticlePost, ArticleCategroy


class ArticleCategroyModelSerializer(ModelSerializer):
    """
    文章分类模型序列化器
    """
    class Meta:
        model = ArticleCategroy
        fields = ('id', 'name')


class ArticlePostModelSerializer(ModelSerializer):
    """
    文章
    """
    class Meta:
        model = ArticlePost
        fields = ('id', 'title', 'about_aritcle', 'article_picture')
