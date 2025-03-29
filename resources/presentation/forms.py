from django import forms

class ResourceForm(forms.Form):
    name = forms.CharField(max_length=100)
    type = forms.CharField(max_length=50)
    status = forms.CharField(max_length=20)
