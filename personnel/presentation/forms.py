from django import forms

class PersonnelForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    role = forms.CharField(max_length=50)
    email = forms.EmailField()
