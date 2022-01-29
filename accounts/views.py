from ast import Not
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages, auth
from emails.models import BulkEmail

def register(request):
    if request.method == 'POST':
        # register user
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # check if passwords match
        if password != password2:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'accounts/register.html')
        # check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
            return render(request, 'accounts/register.html')
        # check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return render(request, 'accounts/register.html')
        user = User.objects.create_user(username=username, email=email, password=password)
        auth.login(request, user=user)
        messages.success(request, 'Successfully logged in!')
        return redirect('dashboard')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        # login user
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user=user)
            messages.success(request, 'Successfully logged in!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials!')
            return render(request, 'accounts/login.html')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        # logout user
        auth.logout(request)
        messages.success(request, 'Successfully logged out!')
        return render(request, 'accounts/login.html')
    else:
        return render(request, 'accounts/login.html')
        
def dashboard(request):
    sent_emails = BulkEmail.objects.filter(user_id=request.user.id)

    context = {
        'sent_emails': sent_emails
    }
    return render(request, 'accounts/dashboard.html', context)
        