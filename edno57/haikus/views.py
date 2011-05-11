from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import *
from haikus.models import Haiku

def homepage(request):
    latest_haikus = Haiku.objects.all()[0:50]

    return TemplateResponse(request, "homepage.html", locals())


def user_page(request, username):
    user = get_object_or_404(User, username = username)

    haikus = user.haiku_set.all()

    is_me = request.user == user

    return TemplateResponse(request, "userpage.html", locals())


@login_required
def add_haiku(request):
    if request.method == "POST":
        haiku = Haiku(user = request.user, text = request.POST.get('text'))
        haiku.save()

    return redirect('user-page', username = request.user.username)
