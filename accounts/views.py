from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, "accounts/login.html")


def signup(request):
    return render(request, "accounts/signup.html")


def logout(request):
    # TODO need to route to homepage, and make sure to logout
    return render(request, "accounts/signup.html")
