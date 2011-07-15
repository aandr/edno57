from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField()

    def clean_name(self):
        text = self.cleaned_data['name']
        if text != text.upper():
            raise forms.ValidationError("PLEASE WRITE YOUR NAME IN ALL CAPS!!!")
