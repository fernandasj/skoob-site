from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import RegisterUser
from .models import Profile


def registerUser(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form['username'].value(),
                email=form['email'].value(),
                password=form['password'].value())
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('users:login')
    else:
        form = RegisterUser()
        print(form.errors)
    return render(request, 'registration/cadastro.html', {'form': form})


@login_required
def profile(request):
    profiles = Profile.objects.filter(user=request.user)
    return render(request, 'registration/profile.html', {'profiles': profiles})
