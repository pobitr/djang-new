from django import forms
from django.core import validators

class FormName(forms.Form):
	name = forms.CharField()
	email_verify = forms.EmailField(label='Enter Email again:')
	text = forms.CharField(widget=forms.Textarea)
	
	
