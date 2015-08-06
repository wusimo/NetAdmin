from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index_page_view),
    url(r'^tota/', views.tota_page_view),
    url(r'^toparents/', views.toparents_page_view),
    url(r'^tostudent/',views.tostudent_page_view),
    url(r'^translate/', views.translate_page_view),
    url(r'^studentinfo/', views.studentinfo_page_view),
]
