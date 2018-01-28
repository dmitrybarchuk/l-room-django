# coding: utf-8
from django.core.mail import send_mail
from django.forms import forms

from project import settings


class EmailMessageForm(forms.Form):

    class Meta:
        exclude = ()

    def is_valid(self):

        if super(EmailMessageForm, self).is_valid():
            if self.data['name']:
                return False

            return True

    def send_email(self):

        send_mail(u'Сообщение с сайта LIVING ROOM', self.data['message'], settings.MAIL_SENDER, [settings.RECIPIENT])
