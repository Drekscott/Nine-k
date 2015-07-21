from django.conf.urls import url
from ninek_site import views

urlpatterns = [
    url(r'$', views.index, name='index'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
]
