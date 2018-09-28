from django.conf.urls import url
from . import views

urlpatterns = [

    #r'^$'匹配空字符串,也就是http://127.0.0.1:8000
    # name='post_list' 是 URL 的名字，用来唯一标识对应的 view。 它可以跟 view 的名字一样，也可以完全不一样
    url(r'^$',views.post_list,name='post_list'),

    #url(r'^post/(?P<pk>[0-9]+)/$',views.post_detail,name='post_detail')
    #也可以写成
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),

    url(r'^post/new/$',views.post_new,name='post_new'),

    url(r'^post/(?P<pk>[0-9]+)/edit/$',views.post_edit,name='post_edit'),

    url(r'^post/(?P<pk>[0-9]+)/delete/$',views.post_delete,name='post_delete')
]