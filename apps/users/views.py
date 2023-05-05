from django.shortcuts import render, HttpResponseRedirect
from apps.users.forms import UserLoginForm
from django.contrib import auth
from django.urls import reverse


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(
                    request=request,
                    user=user,
                )
                return HttpResponseRedirect(reverse("index"))
    else:
        form = UserLoginForm()

    context = {
        "title": "Log in",
        "form": form,
    }
    return render(request=request, template_name="users/login.html", context=context)


def registration(request):
    context = {
        "title": "Create account",
    }
    return render(
        request=request,
        template_name="users/register.html",
        context=context,
    )
