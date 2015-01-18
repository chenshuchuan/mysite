#coding=utf-8
from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from account.models import User

#定义注册表单模型
class UserForm(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    passworld = forms.CharField(label='密码：',widget=forms.PasswordInput())
    email = forms.EmailField(label='电子邮件：')

#定义登录表单模型
class LoginForm(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    password = forms.CharField(label='密码：',widget=forms.PasswordInput())

#登录
def login(request):
    if request.method == 'POST':
        uf = LoginForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                return render_to_response('success.html',{'username':username,'msg':'登陆成功'})
            else:
                return HttpResponseRedirect('/account/login')
    else:
        uf = LoginForm()
    return render_to_response('login.html',{'uf':uf})

#注册
def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            passworld = uf.cleaned_data['passworld']
            email = uf.cleaned_data['email']
            #将表单写入数据库
            user = User()
            user.username = username
            user.passworld = passworld
            user.email = email
            user.save()
            #返回注册成功页面
            return render_to_response('success.html',{'username':username,'msg':'注册成功'})
    else:
        uf = UserForm()
    return render_to_response('register.html',{'uf':uf})