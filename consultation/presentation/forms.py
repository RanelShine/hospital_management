from django import forms

class ConsultationForm(forms.Form):
    patient_id = forms.IntegerField()
    date = forms.DateTimeField()
    notes = forms.CharField(widget=forms.Textarea, required=False)
