from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Message
from .forms import CustomUserCreationForm, MessageForm


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
        return render(request, 'authenticate/login.html', {'form':fm})

def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/login')
    else:
        fm = CustomUserCreationForm()
    return render(request, 'authenticate/signup.html', {'form':fm})

def log_out(request):
    logout(request)
    return redirect("/login")

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'authenticate/home.html', {'username':request.user})
    else:
        return redirect('/login')


def profile_view(request, username):
    user = get_object_or_404(CustomUser, username=username)
    return render(request, 'authenticate/profile_view.html', {'user': user})

@login_required
def edit_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)

    if request.user != user:
        return redirect('profile_view', username=username)  # Prevent editing others' profiles

    if request.method == 'POST':
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.college = request.POST.get('college', user.college)
        user.bio = request.POST.get('bio', user.bio)
        user.year_of_study = request.POST.get('year_of_study', user.year_of_study)
        user.skills = request.POST.get('skills', user.skills)
        if request.FILES.get('profile_picture'):
            user.profile_picture = request.FILES.get('profile_picture')
        user.save()
        return redirect('profile_view', username=username)
    
    return render(request, 'authenticate/edit_profile.html', {'user': user})




def user_profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'authenticate/user_profile.html', {'user': user})



# View to see the inbox of received messages
@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user).order_by('-sent_at')
    return render(request, 'authenticate/inbox.html', {'messages': messages})

# View to send a new message
@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user  # Set the sender as the current user
            message.save()
            return redirect('inbox')  # Redirect to inbox after sending the message
    else:
        form = MessageForm()

    return render(request, 'authenticate/send_message.html', {'form': form})

    # View to see details of a single message
@login_required
def message_detail(request, id):
    message = get_object_or_404(Message, id=id, receiver=request.user)
    message.read = True  # Mark the message as read
    message.save()
    return render(request, 'authenticate/message_detail.html', {'message': message})