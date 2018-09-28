from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from django.utils import timezone
from .form import PostForm

# Create your views here.
def post_list(request):
    posts=Post.objects.filter(publish_date__lte=timezone.now()).order_by('create_date')
    return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})

def post_new(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if(form.is_valid()):
            post=form.save(commit=False)
            post.author=request.user
            post.publish_date=timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk) #这里重定向到url: post_detail
    else:
        form=PostForm()
        print('as_p',form.as_p())
    return render(request,'blog/post_edit.html',{'form':form})

def post_edit(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        form=PostForm(request.POST,instance=post)
        if(form.is_valid()):
            post=form.save(commit=False)
            post.author=request.user
            post.publish_date=timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=PostForm(instance=post)
    return render(request,'blog/post_edit.html',{'form':form})

def post_delete(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if post:
        post.delete()
        return redirect('post_list')
    else:
        return render(request, 'blog/post_detail.html', {'post': post})