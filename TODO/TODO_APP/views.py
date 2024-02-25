from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout 
from.models import todo
# Create your views here.
def home(request):
    if request.POST:
        user=request.user
        task=request.POST['todo']
        
        new_todo = todo.objects.create(user=user,todo_name=task)
        new_todo.save()
        
        todos=todo.objects.all()
        return render(request,'index.html',{'todos':todos})
    todos=todo.objects.all()
    return render(request,'index.html',{'todos':todos})

def logout_user(request):
    logout(request)
    return redirect('login')

def login_user(request):
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('home')
       
    return render(request,"login.html")

def signup(request):
    if request.POST:
        firstname=request.POST['fname']
        
        
        lastname=request.POST['sname']
        username=request.POST['email']
        password=request.POST['password']
      
        new_user=User.objects.create_user(first_name=firstname,last_name= lastname,username=username,password=password)
        new_user.save()
        return redirect('login')
    return render(request,'signup.html')