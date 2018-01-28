# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import FormView

from project import settings
from website.forms import EmailMessageForm
from website.models import Category


def category(request, cat=None):
    template = 'index.html'
    context = {}

    if cat:
        template = 'category.html'
        context['cat'] = get_object_or_404(Category, slug=cat)

    return render(request, template, context)


class EmailMessage(FormView):
    form_class = EmailMessageForm

    def form_valid(self, form):
        form.send_email()
        messages.add_message(self.request, messages.SUCCESS, u'Ваше сообщение отправлено')
        return super(EmailMessage, self).form_valid(form)

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', '/')
