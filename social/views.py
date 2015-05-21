from django.contrib.auth import  login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from social.forms import UserForm, UserProfileForm, FeedbackForm, SearchForm
from social.models import UserProfile, Feedback


def home(request):
    if request.user.is_authenticated():
        return redirect("person", person_id=request.user.id)
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
            if not userprofile.is_doctor and userprofile.doctor_type:
                userprofile.doctor_type = ""

            userprofile.save()

            login(request, authenticate(username=uf.cleaned_data['username'], password=uf.cleaned_data['password']))

            return redirect("home")
    else:
        uf = UserForm(prefix='user')
        upf = UserProfileForm(prefix='userprofile')
    return render(request, 'registration/register.html', dict(userform=uf, userprofileform=upf))


def person(request, person_id, feedback_form=None):
    person = UserProfile.objects.get(user=person_id)
    if person.is_doctor:
        feedbacks = Feedback.objects.filter(estimated=person)
    else:
        feedbacks = Feedback.objects.filter(author=person)

    feedback_form = feedback_form or FeedbackForm()
    return render(request, "person.html", {"person": person, "feedbacks": feedbacks, "form": feedback_form})

def search(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        persons = User.objects.filter(username__contains=form.cleaned_data.get("username"))
        return render(request, "search.html", {'persons': persons})
    else:
        return redirect("home")


def search_doctors(request):
    return render(request, "search.html", {'persons': User.objects.filter(userprofile__is_doctor=True)})


@login_required
def send_feedback(request, person_id):
    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback = feedback_form.save(commit=False)
            feedback.author = request.user.userprofile
            feedback.estimated = UserProfile.objects.get(id=person_id)
            feedback.save()
    return redirect("person", person_id=person_id)

@login_required
def person_follow(request, person_id):
    request.user.userprofile.following.add(UserProfile.objects.get(user=person_id))
    return redirect("person", person_id=person_id)

@login_required
def person_unfollow(request, person_id):
    request.user.userprofile.following.remove(UserProfile.objects.get(user=person_id))
    return redirect("person", person_id=person_id)

