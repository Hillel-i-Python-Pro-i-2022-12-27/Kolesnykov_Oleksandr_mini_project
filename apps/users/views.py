from django.shortcuts import render


def login(request):
    return render(request=request, template_name="users/login.html")


def registration(request):
    context = {
        "title": "Create account",
    }
    return render(
        request=request,
        template_name="users/register.html",
        context=context,
    )
