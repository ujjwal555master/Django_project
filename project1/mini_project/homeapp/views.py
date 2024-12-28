from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'home/index.html', {'name':request.user})
    else:
        return redirect('/login')

