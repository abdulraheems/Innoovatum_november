from django import forms
from .models import Website

class WebsiteForm(forms.ModelForm):
  class Meta:
    model = Website
    fields = ["website_title", "website_link","website_content"]
    labels = {'website_title': "Website Name", "website_link": "Website Link", "website_content": "Website Description"}

    widgets = {
            'website_title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Eg : Innoovatum'}),
            'website_link': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Eg: https://innoovatum.com'}),
            'website_content': forms.Textarea(attrs={'class':'form-control', 'rows':'6'}),
            
        }        