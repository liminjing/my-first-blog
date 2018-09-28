from .models import Post
from django import forms

class PostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields={'title','text',}    #为避免顺序颠倒，最后面加逗号