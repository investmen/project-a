from django.conf.urls import url
from . import views
urlpatterns=[url(r'^$', views.index, name = 'index'),
             url(r'^harini/$', views.harini, name = 'harini'),
             url(r'^topic/(?P<topic_id>[0-9]+)/post/(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
             url(r'^topic/(?P<topic_id>[0-9]+)/post/list/$', views.post_list_html, name = 'list'),
             url(r'^topic/(?P<topic_id>[0-9]+)/$', views.topic_detail, name='topic_detail'),
             url(r'^topic/list/$', views.topic_list, name='topic_list'),
             url(r'^topic/create/$',views.topic_create, name='topic_create'),
             url(r'^topic/(?P<topic_id>[0-9]+)/post/create/$', views.post_create, name='post_create'),]

