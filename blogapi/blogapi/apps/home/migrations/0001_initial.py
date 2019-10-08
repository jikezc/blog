# Generated by Django 2.2.5 on 2019-09-29 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slideshow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort', models.IntegerField(verbose_name='显示顺序')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否上架')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否逻辑删除')),
                ('create_time', models.TimeField(auto_now_add=True, verbose_name='新增时间')),
                ('update_time', models.TimeField(auto_now=True, verbose_name='更新时间')),
                ('image', models.ImageField(blank=True, null=True, upload_to='slideshow', verbose_name='轮播图')),
                ('name', models.CharField(max_length=150, verbose_name='轮播图名称')),
                ('note', models.CharField(blank=True, max_length=150, null=True, verbose_name='备注信息')),
                ('link', models.CharField(blank=True, max_length=150, null=True, verbose_name='轮播图广告地址')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
                'db_table': 'blog_slideshow',
            },
        ),
    ]
