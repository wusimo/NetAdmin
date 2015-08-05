from django.conf.urls import include, url
from Student import views

urlpatterns = [
    url(r'^$', views.email_page_view),
    url(r'^email/', views.email_page_view),
    url(r'^toadmin/', views.toadmin_page_view),
    url(r'^tota/', views.tota_page_view),
    url(r'^toparents/', views.toparents_page_view),
    url(r'^toprof/', views.toprof_page_view),
]
