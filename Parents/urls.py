from django.conf.urls import include, url
from Parents import views

urlpatterns = [,
    url(r'^tostudent', views.tostudent_page_view),
    url(r'^toadmin', views.toadmin_page_view),
    url(r'^toschool', views.toschool_page_view),
    url(r'^aboutstudent', views.aboutstudent_page_view),
]