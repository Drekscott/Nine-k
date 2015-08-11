from django.conf.urls import url
from ninek_site import views
from views import MediaListView, MediaDetailView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^page/(?P<page_name_slug>[\w\-]+)/$', views.page, name='page'),
    url(r'^media/$', MediaListView.as_view(), name='media'),
    url(r'^media/(?P<pk>[0-9]+)/$', MediaDetailView.as_view(), name='media-detail'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
