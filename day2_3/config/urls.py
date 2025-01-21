
from django.contrib import admin
from django.urls import path, include
from todo.views import todo_list,todo_info
from users.views import signup,login



urlpatterns = [
    path("todo/", todo_list, name="todo_list"),

    path("admin/", admin.site.urls),

    path("<int:todo_id>/",todo_info,name="todo_info"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/login/",login,name="login"),
    path("accounts/signup/",signup,name="signup"),
]