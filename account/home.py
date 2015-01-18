#coding=utf-8
from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from account.models import User

def home(request):
    print "22222222222222222222"
    user = User.objects.all()
    print "33333333333333333333"
    print user
    return render_to_response('home.html',{'hello':'hello world'})
