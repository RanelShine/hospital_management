from django.shortcuts import render, get_object_or_404, redirect
from patient.data.models import Patient
from patient.presentation.forms import PatientForm

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient/patient_list.html', {'patients': patients})

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patient/patient_detail.html', {'patient': patient})

def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            from patient.business.services import create_patient
            patient = create_patient(form.cleaned_data)
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = PatientForm()
    return render(request, 'patient/patient_form.html', {'form': form})
