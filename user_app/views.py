from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from user_app.models import Project

# Create your views here.
# 主要代码逻辑


def index(request):
    return render(request, "index.html")


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        if username == "" or password == "":
            return render(request, "index.html", {"error": "用户名或密码为空"})
        else:
            user = auth.authenticate(username=username, password=password)  # 验证用户是否存在

            if user is not None:
                auth.login(request, user)  # 记录用户登录状态， 与login_required配合使用
                request.session['user'] = username
                return HttpResponseRedirect("/project_manage/")
            else:
                return render(request, "index.html", {"error": "用户名或密码错误"})


@login_required  # 判断用户是否登录
def project_manage(request):
    username = request.session.get('user')
    project_all = Project.objects.all()
    print(project_all)
    return render(request, "project_manage.html", {
        "user": username,
        "projects": project_all
    })


def logout(request):
    auth.logout(request)  # 清除用户登录状态
    response = HttpResponseRedirect('/')
    return response
