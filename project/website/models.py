# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

import cStringIO
from PIL import ImageFilter, Image
from django.core.mail import send_mail
from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail

from project import settings


def get_upload_path(self, filename=None):
    return os.path.join("galleries", "%s" % self.images.slug if hasattr(self, 'images') else self.slug, filename)


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'Заголовок категории')
    slug = models.SlugField(max_length=50)
    main_image = ImageField(upload_to=get_upload_path, verbose_name=u'Изображение категории')
    show_in_slider = models.BooleanField(default=True, verbose_name=u'Показывать в слайдере?')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'


class ImageCategory(models.Model):
    image = ImageField(u'Изображение', upload_to=get_upload_path)
    category = models.ForeignKey(Category, name='images')

    def get_base64_blurred_preview(self):
        thumb = get_thumbnail(self.image, '100x75', crop='10%', quality=10)
        image = Image.open(thumb)
        image = image.filter(ImageFilter.GaussianBlur)
        buffer = cStringIO.StringIO()
        image.save(buffer, format="JPEG")
        return u'data:image/jpeg;base64,%s' % buffer.getvalue().encode("base64").replace('\n', '')


class EmailMessage(models.Model):
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = u'Сообщение с сайта'
        verbose_name_plural = u'Сообщения с сайта'

    def __unicode__(self):
        return '%s - %s' % (self.email, self.message[:50])
