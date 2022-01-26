from distutils.command.upload import upload
from django import forms

class SendEmailForm(forms.Form):
    title = forms.CharField()
    subject = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    file = forms.FileField()