# Generated by Django 2.2.5 on 2019-10-08 07:52

from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategroy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort', models.IntegerField(verbose_name='显示顺序')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否上架')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否逻辑删除')),
                ('create_time', models.TimeField(auto_now_add=True, verbose_name='新增时间')),
                ('update_time', models.TimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=255, verbose_name='分类名称')),
            ],
            options={
                'verbose_name': '文章分类表',
                'verbose_name_plural': '文章分类表',
                'db_table': 'tb_article_categroy',
            },
        ),
        migrations.CreateModel(
            name='ArticlePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort', models.IntegerField(verbose_name='显示顺序')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否上架')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否逻辑删除')),
                ('create_time', models.TimeField(auto_now_add=True, verbose_name='新增时间')),
                ('update_time', models.TimeField(auto_now=True, verbose_name='更新时间')),
                ('author', models.CharField(max_length=25, verbose_name='作者')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('about_aritcle', models.TextField(verbose_name='概要')),
                ('article_body', mdeditor.fields.MDTextField(verbose_name='正文')),
                ('views_count', models.IntegerField(verbose_name='文章浏览量')),
                ('give_like_count', models.IntegerField(verbose_name='点赞数')),
                ('article_picture', models.ImageField(blank=True, null=True, upload_to='articleimage', verbose_name='文章图片')),
                ('article_categroy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.ArticleCategroy', verbose_name='文章分类')),
            ],
            options={
                'verbose_name': '文章表',
                'verbose_name_plural': '文章表',
                'db_table': 'tb_atricle_post',
            },
        ),
    ]