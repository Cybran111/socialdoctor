from django.shortcuts import render, redirect

# Create your views here.
from social.forms import UserForm, UserProfileForm


def home(request):
    return render(request, "base.html")


def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, prefix='user')
        upf = UserProfileForm(request.POST, prefix='userprofile')
        if uf.is_valid() and upf.is_valid():
            user = uf.save(commit=False)
            user.set_password(uf.cleaned_data['password'])
            user.save()

            userprofile = upf.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return redirect("home")
    else:
        uf = UserForm(prefix='user')
        upf = UserProfileForm(prefix='userprofile')
    return render(request, 'registration/register.html', dict(userform=uf, userprofileform=upf))