from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def login(request):
    return render(request, "auth/login.html", {})


def register(request):

    if request.method == "POST":
        email = request.post["email"].replace(" ", "").lower()
        password1 = request.post["password1"]
        password2 = request.post["password2"]

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "A user with this email already exists")
            return redirect("register")

        newUser = User.objects.create_user(
            email=email, username=email, password=password1
        )
        newUser.save()

        auth.login(request, newUser)
        return redirect("home")

    return render(request, "auth/register.html", {})
