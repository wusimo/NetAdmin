from django.conf.urls import include, url
from TA import views

urlpatterns = [
    url(r'^papers', views.papers_page_view),
    url(r'^tostudent/(?P<student_id>[0-9]+)/$', views.tostudent_page_view),
]