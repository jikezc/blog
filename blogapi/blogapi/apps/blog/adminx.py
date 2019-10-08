import xadmin
from .models import ArticlePost, ArticleCategroy, Messages


class ArticlePostModelAdmin(object):
    """
    文章模型管理类
    """
    pass


xadmin.site.register(ArticlePost, ArticlePostModelAdmin)


class AricleCategroyModelAdmin(object):
    """
    文章分类模型管理类
    """
    pass


xadmin.site.register(ArticleCategroy, AricleCategroyModelAdmin)


class MessageModelAdmin(object):
    """
    留言板模型管理类
    """
    pass

xadmin.site.register(Messages, MessageModelAdmin)