from django.conf.urls import url
from . import views
from NetAdmin.views import message_page_view

urlpatterns = [
    url(r'^$', views.index_page_view),
    url(r'^toadmin/', views.toadmin_page_view),
    url(r'^toadmin/([0-9]+)/$', message_page_view),
    url(r'^papers/', views.papers_page_view),
    url(r'^finishedpapers/', views.finishedpapers_page_view),
    url(r'^tostudent/', views.tostudent_page_view),
    url(r'^tostudent/([0-9]+)/$', message_page_view),
]

