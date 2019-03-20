from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class ArticleForm(forms.Form):
    title = forms.TextInput(attrs={'help_text':"Enter a Title", 'required':True})
    body = forms.TextInput(attrs={'required':True})

    def clean_title(self):
        data = self.cleaned_data['title']

        #Check if title is too long
        if len(data) > 100:
            raise ValidationError(_('Title is too long. Must be 100 chars or less.'))

        return data