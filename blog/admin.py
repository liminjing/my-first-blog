from django.contrib import admin
from .models import Post

# Register your models here.

#让模型在admin页面上可见
admin.site.register(Post)