# Generated by Django 2.2.5 on 2019-10-11 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideshow',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='新增时间'),
        ),
        migrations.AlterField(
            model_name='slideshow',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]
