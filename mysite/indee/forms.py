from django import forms
from django.core.exceptions import ValidationError

from django.http import HttpResponse


class UploadFileForm(forms.Form):
    upload_file = forms.FileField(
        label='Select a file',
        help_text='Max. 2.5 MB',
        widget=forms.FileInput(attrs={'required': 'true', 'accept':'application/pdf'}),
                                error_messages={'required': 'You can upload PDF files only'},
    )


class NameForm(forms.Form):
    firstName = forms.CharField(label='First name', max_length=100)



