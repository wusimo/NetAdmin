"""NetAdmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from NetAdmin import views as NetAdmin_views

from TA import urls as ta_urls
from Student import urls as student_urls
from Account import urls as account_urls
from Parents import urls as parents_urls
from Agent import urls as admin_urls

urlpatterns = [
    url(r'^$', NetAdmin_views.landing_page_view),
    url(r'^index/', NetAdmin_views.index_page_view),

    url(r'^account/', include(account_urls)),

    url(r'^student/', include(student_urls)),
    url(r'^parents/', include(parents_urls)),
    url(r'^agent/', include(admin_urls)),
    url(r'^ta/', include(ta_urls)),


    url(r'^admin/', include(admin.site.urls)),
]
