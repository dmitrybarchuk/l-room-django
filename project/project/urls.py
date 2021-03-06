"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from project import settings
from website import views
from website.views import EmailMessage, CategoryList

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', CategoryList.as_view(), name='category'),
    url(r'^(?P<cat>[\w\d-]+)/$', CategoryList.as_view(), name='category'),
    # url(r'^$', views.category, name='category'),
    url(r'^email-message/$', EmailMessage.as_view(), name='email_message'),
    # url(r'^(?P<cat>[\w\d-]+)/$', views.category, name='category'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


