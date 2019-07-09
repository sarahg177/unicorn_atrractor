from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully')
            user = authenticate(username=request.POST['username'],
                                password1=request.POST['password1'])
            login(request, user)
            return redirect(reverse('ticket_list'))

    return render(request, 'register.html', {'form': form})
