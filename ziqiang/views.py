# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def add(request):
    print(request.is_ajax()) #判断是否是ajax请求
    a=request.GET['a']
    b=request.GET['b']
    c=int(a)+int(b)
    return HttpResponse(str(c))

def add2(request,a,b):
    c=int(a)+int(b)
    return HttpResponse(str(c))


# def index(request):
#     return render(request,'ziqiang/home.html')


# index加上表单提交功能
from .form import AddForm

def index(request):
    if request.method=='POST': #当提交表单时
        form=AddForm(request.POST) #form包含提交的数据
        if form.is_valid(): #如果提交的数据合法
            a=form.cleaned_data['a']
            b=form.cleaned_data['b']
            return HttpResponse(str(int(a)+int(b)))
    else:   #正常访问时
        form=AddForm()
    return render(request,'ziqiang/home.html',{'form':form})


from django.core.mail import send_mail

def email_to(request):
    if request.method=='POST':
        email_to = request.POST['email_to']
        content = request.POST['content']
        print(email_to, content)

        result_code=send_mail('this is a mail from test', content, 'maggy_li@163.com',
                  [email_to], fail_silently=False)
        if 1==result_code:
            return HttpResponse('send success!')
        else:
            return HttpResponse('send fail!')

from django.http import JsonResponse

#加载列表
def ajax_list(request):
    i=[i for i in range(10,30)]
    return JsonResponse(i,safe=False) #TypeError: In order to allow non-dict objects to be serialized set the safe parameter to False.

#加载字典
def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)

#加载复杂列表
def ajax_list_dict(request):
    person_info_dict = [
        {"name": "xiaoming", "age": 20},
        {"name": "tuweizhong", "age": 24},
        {"name": "xiaoli", "age": 33},
    ]
    return JsonResponse(person_info_dict,safe=False)