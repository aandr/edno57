from django.template.response import TemplateResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from haikus.models import Haiku
from haikus.forms import NewHaikuForm


def homepage(request):
    latest_haikus = Haiku.objects.all().order_by('-created')[:50]
    form = NewHaikuForm(request.POST or None)
    if request.user.is_authenticated():
        form.user = request.user
        if form.is_valid():
            form.save()
    return TemplateResponse(request, 'homepage.html', locals())


def user_page(request, username):
    user = get_object_or_404(User, username=username)
    haikus = user.haiku_set.all()
    return TemplateResponse(request, 'userpage.html', locals())
