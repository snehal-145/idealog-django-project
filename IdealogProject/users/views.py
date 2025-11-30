from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
import re

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! Please login.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def register_view(request):
    """
    Function-based view to handle user registration using Django's
    built-in UserCreationForm. On successful registration redirects
    to the login page. On GET or invalid POST it renders
    'users/register.html' with the form and any validation errors.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # additional server-side validation (no hint in form, only error messages)
            username = form.cleaned_data.get('username', '')
            password1 = form.cleaned_data.get('password1', '')

            # username: allow letters, numbers, underscores, 3-30 chars
            if not re.match(r'^[A-Za-z0-9_]{3,30}$', username):
                form.add_error('username', 'Enter a valid username (letters, numbers and _).')

            # password: at least 8 chars, includes letters and numbers
            if not re.search(r'(?=^.{8,}$)(?=.*[A-Za-z])(?=.*\d)', password1):
                form.add_error('password1', 'Password must be at least 8 characters and include letters and numbers.')

            if form.errors:
                # render form with errors
                return render(request, 'users/register.html', {'form': form})

            # all validations passed
            form.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def logout_view(request):
    """Log the user out and redirect to the login page."""
    logout(request)
    return redirect('login')
