from django.db import models
from blogapi.utils.basemodels import BaseModel


# Create your models here.

class Slideshow(BaseModel):
    """
    轮播图的模型
    """
    # upload_to 存储子目录，真实存放地址会使用配置中的MADIE_ROOT+upload_to
    image = models.ImageField(upload_to="slideshow", verbose_name="轮播图", null=True, blank=True)
    name = models.CharField(max_length=150, verbose_name='轮播图名称')
    note = models.CharField(max_length=150, verbose_name="备注信息", null=True, blank=True)
    link = models.CharField(max_length=150, verbose_name="轮播图广告地址", null=True, blank=True)

    class Meta:
        db_table = 'blog_slideshow'
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
