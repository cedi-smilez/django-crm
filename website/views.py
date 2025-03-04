from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import sign_up_form

# Create your views here.
def home(request):
    # check to see if user is logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('home')
        else:
            messages.success(request, 'There was an error logging in')
            return redirect('home')
    else:
        return render(request, 'home.html', {})

#def login_user(request):
 #   pass

def logout_user(request):
    logout(request)
    messages.success(request, 'You Have Been Logged Out...')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = sign_up_form(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password = password)
            login(request, user)
            messages.success(request, 'Logged In Successfully')
            return redirect('home')
    else:
        form = sign_up_form()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})