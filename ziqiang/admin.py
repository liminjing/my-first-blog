from django.contrib import admin
from .models import Article


class AriticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_time',) #配置要显示的字段
    search_fields = ('title','content') #搜索功能


# Register your models here.
admin.site.register(Article,AriticleAdmin)