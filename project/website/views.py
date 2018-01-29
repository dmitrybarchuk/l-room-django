# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import FormView, ListView

from project import settings
from website.forms import EmailMessageForm
from website.models import Category, ImageCategory


class CategoryList(ListView):
    model = ImageCategory
    paginate_by = 12

    def get_template_names(self):
        return 'category.html' if self.kwargs.get('cat', None) else 'index.html'

    def get_queryset(self):
        q = super(CategoryList, self).get_queryset()
        if 'cat' in self.kwargs:
            try:
                Category.objects.get(slug=self.kwargs['cat'])
                return q.filter(images__slug=self.kwargs['cat'])
            except Category.DoesNotExist:
                raise Http404(u'Категория не найдена')
        else:
            return q

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        try:
            category_obj = Category.objects.get(slug=self.kwargs.get('cat', None))
            context['cat'] = category_obj
        except Category.DoesNotExist:
            pass
        return context


class EmailMessage(FormView):
    form_class = EmailMessageForm

    def form_valid(self, form):
        form.send_email()
        messages.add_message(self.request, messages.SUCCESS, u'Ваше сообщение отправлено')
        return super(EmailMessage, self).form_valid(form)

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', '/')
