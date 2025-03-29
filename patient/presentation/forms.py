from django import forms

class PatientForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    date_of_birth = forms.DateField()
    email = forms.EmailField()
    phone = forms.CharField(max_length=20, required=False)
