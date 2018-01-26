# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

# Register your models here.
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.forms import FlatpageForm as FlatpageFormOld
from django.contrib.flatpages.models import FlatPage

from website.models import ImageCategory, Category


class ImageCategoryAdmin(admin.TabularInline):
    model = ImageCategory


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = {'slug': ('title',), }
    list_display = ('title', )
    inlines = [ImageCategoryAdmin]


admin.site.register(Category, CategoryAdmin)


class FlatpageForm(FlatpageFormOld):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = FlatPage
        fields = '__all__'


class FlatPageAdmin(FlatPageAdminOld):
    form = FlatpageForm


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
