
from django.contrib import admin
from django.http import Http404
from django.shortcuts import render
from django.urls import path
from fake_db import user_db

db=user_db

def user_list(request):
    user=[{'id':key,'name':value['이름']}for key,value in db.items()]
    return render(request,'user_list.html',{'user':user})

def user_info(request,user_id):
    if user_id >=len(db):
        raise Http404("Not Found")
    data=db[user_id]
    return render(request,'user_info.html',{'data':data})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", user_list, name="user_list"),
    path("users/<int:user_id>/", user_info, name="user_info"),
]
