
from django.contrib import admin
from django.urls import path
from todo.views import todo_list,todo_info
from fake_db import user_db
from django.shortcuts import render,Http404

db=user_db

def user_list(request):
    user=[{'id':key,'name':value['이름']}for key,value in db.items()]

    return render(request,'users/user_list.html',{'user':user})

def user_info(request,user_id):
    if user_id >=len(db):
        raise Http404("Not Found")
    data=db[user_id]
    return render(request,'users/user_info.html',{'data':data})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", user_list, name="user_list"),
    path("users/<int:user_id>/", user_info, name="user_info"),

    path("todo/",todo_list,name="todo_list"),
    path("todo/<int:todo_id>/",todo_info,name="todo_info"),
]
