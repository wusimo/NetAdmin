from django.conf.urls import url
from . import views
from NetAdmin.views import message_page_view

urlpatterns = [
    url(r'^$', views.index_page_view),

    url(r'^tota/$', views.tota_page_view),
    url(r'^tota/(?P<message_id>[0-9]+)/$', views.toparents_page_view),

    url(r'^toparents/$', views.toparents_page_view),
    url(r'^toparents/(?P<message_id>[0-9]+)/$', message_page_view),

    url(r'^tostudent/$',views.tostudent_page_view),
    url(r'^tostudent/(?P<message_id>[0-9]+)/$', message_page_view),

    url(r'^translate/$', views.translate_page_view),
    url(r'^studentinfo/$', views.studentinfo_page_view),
]
