from django.db import models
from blogapi.utils.basemodels import BaseModel
from ckeditor_uploader.fields import RichTextUploadingField
from mdeditor.fields import MDTextField
import markdown


# Create your models here.
class ArticlePost(BaseModel):
    """
    文章内容的模型
    """
    # 文章作者
    author = models.CharField(max_length=25, verbose_name="作者")
    # 文章标题
    title = models.CharField(max_length=255, verbose_name="标题")
    # 文章概要
    about_aritcle = models.TextField(verbose_name="概要")
    # 文章正文
    article_body = MDTextField(verbose_name="正文")
    # 文章浏览量
    views_count = models.IntegerField(verbose_name="文章浏览量")
    # 点赞数
    give_like_count = models.IntegerField(verbose_name="点赞数")
    # 文章类
    article_categroy = models.ForeignKey("ArticleCategroy", on_delete=models.CASCADE, verbose_name="文章分类")
    # 文章图片
    article_picture = models.ImageField(upload_to="articleimage", verbose_name="文章图片", null=True, blank=True)

    class Meta:
        db_table = "tb_atricle_post"
        verbose_name = "文章表"
        verbose_name_plural = verbose_name

    # @property
    # def article_to_html(self):
    #     self.article_body = markdown.markdown(self.article_body,
    #                                           extensions=[
    #                                               # 包含 缩写、表格等常用扩展
    #                                               'markdown.extensions.extra',
    #                                               # 语法高亮扩展
    #                                               'markdown.extensions.codehilite',
    #                                           ])
    #     return self.article_body

    def __str__(self):
        return self.title




class ArticleCategroy(BaseModel):
    """
    文章分类的模型
    """
    # 文章分类称
    name = models.CharField(max_length=255, verbose_name="分类名称")

    class Meta:
        db_table = "tb_article_categroy"
        verbose_name = "文章分类表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Messages(models.Model):
    """留言板的模型"""
    message_content = models.TextField(max_length=255, verbose_name="留言板")

    class Meta:
        db_table = 'tb_messages'
        verbose_name = "留言板"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message_content