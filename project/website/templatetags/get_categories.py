from django.template.defaulttags import register

from website.models import Category


@register.simple_tag
def get_categories():
    return Category.objects.all()
