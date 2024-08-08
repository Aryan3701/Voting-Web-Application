from django.http import HttpResponse
from django.shortcuts import render
from home.models import details
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

def home(request):
    return render(request,'index.html')
def login(request):
    if request.method == "POST":
        user=request.POST.get('username')
        pss=request.POST.get('password')
        if details.objects.filter(name=user,password=pss).exists():
            return render(request,'page.html')
        else:
            return HttpResponse("check your username or password")           
    return render(request,'login.html')
def signup(request):
    if request.method == "POST":
        
        details_instance = details()

        
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        
        details_instance.name = name
        details_instance.email = email
        details_instance.password = password

       
        details_instance.save()

        return redirect('login')

    return render(request, 'signup.html')

