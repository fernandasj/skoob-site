from .models import Profile
from .forms import RegisterUser
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def registerUser(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form['username'].value(),
                             email=form['email'].value(),
                             password=form['password'].value())
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('users:login')
    else:
        form = RegisterUser()
        print (form.errors)
    return render(request, '../templates/registration/cadastro.html', {'form': form})


@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, '../templates/home.html')

@login_required
def UserEdit(request, pk):
     profile = get_object_or_404(Post, pk=pk)
     if request.method == "POST":
         form = RegisterUser(request.POST, instance=post)
         if form.is_valid():
             profile = form.save(commit=False)
             profile.user = request.user
             post.save()
             return redirect('post_detail', pk=post.pk)
     else:
         form = RegisterUser(instance=post)
     return render(request, 'templates/cadastroEdit.html', {'form': form})
