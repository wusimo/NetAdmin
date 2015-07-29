from django.conf.urls import include, url
from Admin import views

urlpatterns = [
    url(r'^tostudent/(?P<student_id>[0-9]+)/$', views.tostudent_page_view),
    url(r'^tostudent/(?P<student_id>[0-9]+)/toschool/$', views.tostudent_toschool_page_view),
    url(r'^tota/(?P<ta_id>[0-9]+)/$', views.tota_page_view),
    url(r'^toparents/(?P<parents_id>[0-9]+)/$', views.toparents_page_view),
    url(r'^dashboard/', views.dashboard_page_view),
]