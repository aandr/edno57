from django.template.response import TemplateResponse
from feedback.forms import ContactForm

def contact_form(request):
    form = ContactForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            name = forms.cleaned_data['name']
            email = forms.cleaned_data['email']
            text = forms.cleaned_data['text']
            # send email with name, email and text
            return redirect('/')

    return TemplateResponse(request, 'feedback.html', {'form': form })


        
