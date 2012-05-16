from django.views.generic import ListView
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import *
from haikus.models import Haiku
from haikus.forms import NewHaikuForm

class Homepage(ListView):
    model = Haiku
    template_name = 'homepage.html'
    paginate_by = 50


class UserPage(ListView):
    model = Haiku
    template_name = 'userpage.html'

    def get_queryset(self):
        return Haiku.objects.filter(user__username=self.kwargs['username'])

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        context['user'] = User.objects.get(username = self.kwargs['username'])
        context['is_me'] = self.request.user == context['user']
        return context

def user_page(request, username):
    user = User.objects.get(username = username)
    is_me = request.user == user
    haiku_list = user.haiku_set.all()
    return TemplateResponse(request, 'userpage.html', locals())

@login_required
def add_haiku(request):
    if request.method != 'POST':
        raise Exception

    haiku = Haiku(user = request.user)
    form = NewHaikuForm(request.POST, instance = haiku)
    form.save()


    return redirect("user-page", username = request.user.username)

