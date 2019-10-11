from rest_framework.serializers import ModelSerializer
from .models import ArticlePost, ArticleCategroy, Messages


class ArticleCategroyModelSerializer(ModelSerializer):
    """
    文章分类模型序列化器
    """
    class Meta:
        model = ArticleCategroy
        fields = ('id', 'name')


class ArticlePostModelSerializer(ModelSerializer):
    """
    文章序列化器
    """
    class Meta:
        model = ArticlePost
        fields = ('id', 'title', 'about_aritcle', 'article_picture')


class ArticleRetrieveModelSerializer(ModelSerializer):
    """文章详情序列化器"""
    class Meta:
        model = ArticlePost
        fields = ('id', 'author', 'title', 'views_count', 'give_like_count', 'article_body', 'create_time')


class MessagesModelSerializer(ModelSerializer):
    """留言板序列化器"""
    class Meta:
        model = Messages
        fields = "__all__"


class GiveLikeModelSerializer(ModelSerializer):
    """点赞序列化器"""
    class Meta:
        model = ArticlePost
        fields = ['id', 'give_like_count']
