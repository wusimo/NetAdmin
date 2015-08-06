from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index_page_view),
    url(r'^toadmin/', views.toadmin_page_view),
    url(r'^papers/', views.papers_page_view),
    url(r'^finishedpapers/', views.finishedpapers_page_view),
    url(r'^tostudent/', views.tostudent_page_view),
]

