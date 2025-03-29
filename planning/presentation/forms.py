from django import forms

class AppointmentForm(forms.Form):
    patient_id = forms.IntegerField()
    date = forms.DateTimeField()
    description = forms.CharField(widget=forms.Textarea, required=False)
