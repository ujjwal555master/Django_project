from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def user_login(request):
    if(request.method == "POST"):
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect("/")
    else:
        fm = AuthenticationForm()
        return render(request, 'login/logins.html', {'form':fm})

def sign_up(request):
    if request.method == 'POST':
        fm = UserCreationForm(request.POST)
        if(fm.is_valid()):
            messages.success(request, "Account successfull create")
            fm.save()
            print(fm)
    else:
        fm = UserCreationForm()
    return render(request, 'login/signup.html', {'form':fm})

def log_out(request):
    logout(request)
    return redirect("/login")
    