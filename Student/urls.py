from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index_page_view),
    url(r'^email/', views.index_page_view),
    url(r'^toadmin/', views.toadmin_page_view),
    url(r'^tota/', views.tota_page_view),
    url(r'^toparents/', views.toparents_page_view),
    url(r'^toprof/', views.toprof_page_view),
]
