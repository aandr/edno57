from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import *
from haikus.models import Haiku
from haikus.forms import NewHaikuForm

def homepage(request):
    latest_haikus = Haiku.objects.all().order_by('-created')[0:50]

    return TemplateResponse(request, 'homepage.html', locals())

def user_page(request, username):
    user = User.objects.get(username = username)
    is_me = request.user == user
    haikus = user.haiku_set.all()
    return TemplateResponse(request, 'userpage.html', locals())

@login_required
def add_haiku(request):
    if request.method != 'POST':
        raise Exception

    haiku = Haiku(user = request.user)
    form = NewHaikuForm(request.POST, instance = haiku)
    form.save()


    return redirect("user-page", username = request.user.username)

