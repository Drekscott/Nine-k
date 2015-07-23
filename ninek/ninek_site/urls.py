from django.conf.urls import url
from ninek_site import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^page/(?P<page_name_slug>[\w\-]+)/$', views.page, name='page'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
