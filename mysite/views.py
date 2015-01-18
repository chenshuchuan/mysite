#coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from account.models import User
from django.core.paginator import Paginator

def home(request):
    user = User.objects.all()
    user_list = []
    page_size = 2
    
    for u in user:
    	user_context = (int(u.id),u.username,u.email,u.age,u.num)

    	user_list.append(user_context)
 	print "=========user_list========"
 	#print user_list
 	#user_list.sort(reverse = False)	
 	print '===============ul==========='
    #user_list.sort(reverse=True)
    user_list = sorted(user_list, reverse=True, key=lambda user_list : user_list[4])
 	#user_list = sorted(user_list, key=itemgetter(3), reverse=True)
    print '============count_num===='
    print len(user_list)
    return render_to_response('home.html',{'user_list': user_list})
