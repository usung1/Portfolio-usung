from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
import os
from django.conf import settings
from django.http import HttpResponse

def login_view(request):
    message = request.GET.get('abc')
    print(message)

    return HttpResponse("안녕?")

    # if request.user.is_authenticated:
    #     return redirect("/posts/feeds/")

    # if request.method == "POST":
    #     form = LoginForm(data=request.POST)

    #     # LoginForm에 전달된 데이터가 유효하다면
    #     if form.is_valid():
    #         # username과 password 값을 가져와 변수에 할당
    #         username = form.cleaned_data["username"]
    #         password = form.cleaned_data["password"]

    #         # username, password에 해당하는 사용자가 있는지 검사
    #         user = authenticate(username=username, password=password)

    #         # 해당 사용자가 있다면
    #         if user:
    #             # 로그인 처리 후, 피드 페이지로 redirect
    #             login(request, user)
    #             return redirect("/posts/feeds/")
    #         else:
    #             form.add_error(None, "입력한 자격증명에 해당하는 사용자가 없습니다. ")

    #     # 어떤 경우든 실패한 경우(데이터 검증, 사용자 검사 과정에서) 다시 LoginForm을 사용한 로그인 페이지 렌더링
    #     context = {"form": form}
    #     return render(request, "PortfolioA/users/login.html", context)
    # else:
    #     form = LoginForm()
    #     context = {"form": form}
    #     return render(request, "PortfolioA/users/login.html", context)