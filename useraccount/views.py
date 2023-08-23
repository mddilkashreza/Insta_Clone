from django.shortcuts import render, reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from useraccount.forms import SignUpForm,CustomLoginForm
# Create your views here.


def user_login(request):
    form = CustomLoginForm(request.POST or None) #AuthenticationForm first and last customlogin
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        print(user)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("post:home"))
        else :
            errors = form.get_invalid_login_error()
            for error in errors:
                messages.add_message(request, messages.ERROR, (" I can't let you in bro remember your user and password"))
            # print(form.get_invalid_login_error())
    context = {"form": form}
    return render(request,'login.html',context)



def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("user:login"))




def signup(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("user:login"))
    # messages.add_message(request, messages.success,("Register Success"))
    messages.success(request, 'Register Successfully')
    context = {"form": form}
    return render(request, "sign_up.html", context)

