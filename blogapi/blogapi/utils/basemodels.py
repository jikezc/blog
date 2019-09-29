from django.db import models

class BaseModel(models.Model):
    sort = models.IntegerField(verbose_name="显示顺序")
    is_show = models.BooleanField(verbose_name="是否上架", default=False)
    is_delete = models.BooleanField(verbose_name="是否逻辑删除", default=False)
    create_time = models.TimeField(auto_now_add=True, verbose_name="新增时间")
    update_time = models.TimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        # 设置当前模型在数据迁移的时候不要为它创建表
        abstract = True
