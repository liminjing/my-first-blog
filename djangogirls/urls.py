"""djangogirls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from ziqiang import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #把访问'http://127.0.0.1:8000/'的请求转到 blog.urls
    url(r'',include('blog.urls')),

    #ziqiang test

    #采用url—— http://localhost:8000/test/add/?a=4&b=11
    path('test/add/', views.add, name='add'),

    #采用url——http://localhost:8000/test/add/7/8
    path('test/add/<int:a>/<int:b>',views.add2,name='add2'), # django 2.0+
    #url(r'^add/(\d+)/(\d+)/$', calc_views.add2, name='add2'), # django 1.8+

    path('test', views.index, name='index'),

    path('email_to',views.email_to,name='email_to'),

    path('ajax_list',views.ajax_list,name='ajax_list'),

    path('ajax_dict',views.ajax_dict,name='ajax_dict'),

    path('ajax_list_dict',views.ajax_list_dict,name='ajax_list_dict')
]
