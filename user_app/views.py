from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth

# Create your views here.
# 主要代码逻辑


def index(request):
    return render(request, "index.html")


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        # print(username)
        # print(isinstance(username, None))
        # print(type(username))
        # print(type(""))

        if username == "" or password == "":
            return render(request, "index.html", {"error": "用户名或密码为空"})
        else:
            user = auth.authenticate(username=username, password=password)
            print(user)
            print(type(user))
            if user is not None:
                auth.login(request, user)
                return render(request, "project_manage.html")
            else:
                return render(request, "index.html", {"error": "用户名或密码错误"})

        # if username == "admin" and password == "123456":
        #     return render(request, "project_manage.html")
        # else:
        #     return render(request, "index.html", {"error": "用户名或密码错误"})

        # return render(request, "index.html")