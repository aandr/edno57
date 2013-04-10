from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView

from haikus.models import Haiku
from haikus.forms import NewHaikuForm


class LoginRequiredMixin:
    """Ensures that user must be authenticated in order to access view."""

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


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
        context = super(UserPage, self).get_context_data(**kwargs)
        context['author'] = self.kwargs['username']
        return context


class AddHaiku(LoginRequiredMixin, CreateView):
    form_class = NewHaikuForm
    success_url = '/'
    template_name = "homepage.html"

    def get_form_kwargs(self):
        kwargs = super(AddHaiku, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
