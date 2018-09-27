from django.conf.urls import url
from . import views

urlpatterns = [

    #r'^$'匹配空字符串,也就是http://127.0.0.1:8000
    # name='post_list' 是 URL 的名字，用来唯一标识对应的 view。 它可以跟 view 的名字一样，也可以完全不一样
    url(r'^$',views.post_list,name='post_list')
]