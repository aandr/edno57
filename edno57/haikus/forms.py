# -*- coding: utf-8 -*-
import pdb
from django import forms
from haikus.models import Haiku

class NewHaikuForm(forms.ModelForm):
    user = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(NewHaikuForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Haiku
        fields = ('text','user')

    def clean_user(self):
        return self.user

    def clean_text(self):
        text = self.cleaned_data['text']
        syllable_count = count_syllables(text)
        if syllable_count != 17:
            raise forms.ValidationError(u"Това не е валидно хайку (има само или цели %s срички)!" % syllable_count)
        return text

def count_syllables(text):
    vowels = list(u'aeouiyаъоуеиюя')
    text = " %s " % text 

    return len([text[x] for x in range(0, len(text)) if text[x] in vowels and text[x-1] not in vowels])
