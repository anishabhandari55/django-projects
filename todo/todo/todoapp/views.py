from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import todo

def home(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        new_todo = todo(user= request.user, todo_name = task)
        new_todo.save()

    all_todos = todo.objects.filter(user = request.user)
    context = {
        'todos': all_todos
    }
    return render(request, 'todoapp/todo.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(password)<6:
            messages.error(request, 'Password must be at least 6 characters long.')

        get_all_users_by_username = User.objects.filter(username=username)
        if get_all_users_by_username:
            messages.error(request, 'Username already exists!')
            return redirect('register')

        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
        messages.success(request, 'User successfully created! Login Now')
        return redirect('login')
    return render(request, 'todoapp/register.html')

def login(request):

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        validate_user = authenticate(username = username, password = password)
        if validate_user is not None:
            login(request, validate_user)
            return redirect('home')
        else:
            messages.error(request, 'User does not exist!')
            return redirect('login')
    return render(request, 'todoapp/login.html')

def logoutPage(request):
    logout(request)
    redirect('login')

@login_required
def DeleteTask(request, name):
    get_todo = todo.objects.get(user = request.user, todo_name = name)
    get_todo.delete()
    return redirect('home')

@login_required
def UpdateTask(request, name):
    get_todo = todo.objects.get(user=request.user, todo_name = name)
    get_todo.status = True
    get_todo.save()
    return redirect('home')
