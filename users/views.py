from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, 'Your account has been created successfully')
            auth_user = authenticate(username=new_user.username,
                                     password=request.POST['password1'])
            login(request, auth_user)
            return HttpResponseRedirect(reverse('ticket_list'))

    return render(request, 'register.html', {'form': form})
