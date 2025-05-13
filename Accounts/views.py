from django.shortcuts import render,redirect,get_object_or_404
from .forms import SignUpForm,LoginForm,ChangePasswordForm,ProfileForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from Ecommerce_Core.models import Profile

@login_required
def edit_profile(request):
    """
    Edit the user's profile.
    
    Fetches the current user's profile and populates the form with their data.
    If the form is valid, the changes are saved and a success message is shown.
    
    """
    profile = get_object_or_404(Profile,user = request.user)
    form = ProfileForm(instance=profile)
    if request.method =='POST':
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile has been updated successfully ...')
            return redirect('home')
    else:
        return render(request,'accounts/profile.html',{'form':form})

    

def update_password(request):
    """
    Allows an authenticated user to update their password.
    
    - Redirects unauthenticated users to the login page.
    - Validates the password change form.
    - On success, saves the new password and re-authenticates the user.
    - Displays appropriate success or error messages.
    """
    
    if not  request.user.is_authenticated:
        messages.warning(request,"You can't access this page with logging in ..")
        return redirect('login')
    
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(user,request.POST)

        if form.is_valid():
            form.save()
            login(request,user)
            messages.success(request,'Password is Updated successfully ..')
            return redirect('home')
        else:
            for error in list(form.errors.values()):
                messages.error(request,error)
            return render(request,'accounts/update_password.html',{'form':form})
    else:
        form = ChangePasswordForm(user)
        return render(request,'accounts/update_password.html',{'form':form})


def log_in(request):
    
    """
    Logs in a user if the credentials are valid.
    Redirects authenticated users and shows messages on success or failure.
    
    """
    if request.user.is_authenticated:
        messages.warning(request,'You logged in already...')
        return redirect('home')
        
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                messages.success(request,'Logged in successfully...')
                return redirect('home')
            else:
                messages.warning(request," User doesn't exist , Register new ...")
                return redirect('register')
        else:
            messages.error(request,'There is an error :(')
            return render(request,'accounts/login.html',{'form':form})
    else:
        form = LoginForm()
        return render(request,'accounts/login.html',{'form':form})
        



@login_required
def log_out(request):
    """
    Logs out the current user and redirects to the homepage.
    """
    logout(request)
    messages.success(request,'Logged out ...')
    return redirect('home')



def register(request):
    """
    Handles user registration with validation and login after success.
    """

    if request.user.is_authenticated:
        messages.warning(request,'You logged in already...')
        return redirect('home')
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,'Registered Successfully...')
            return redirect('home')
        
        else:

            messages.error(request,'There is an error :(')
            return render(request, 'accounts/register.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request,'accounts/register.html',{'form':form})

            

            

