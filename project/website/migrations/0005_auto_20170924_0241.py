# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 02:41
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_category_main_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='show_in_slider',
            field=models.BooleanField(default=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0432 \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0435?'),
        ),
        migrations.AlterField(
            model_name='category',
            name='main_image',
            field=sorl.thumbnail.fields.ImageField(upload_to=website.models.get_upload_path, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0432 \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0435'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=50, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'),
        ),
    ]
