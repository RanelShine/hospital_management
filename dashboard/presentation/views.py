from django.shortcuts import render
from patient.data.models import Patient
from consultation.data.models import Consultation
from planning.data.models import Appointment

def dashboard_view(request):
    total_patients = Patient.objects.count()
    total_consultations = Consultation.objects.count()
    total_appointments = Appointment.objects.count()
    context = {
        'total_patients': total_patients,
        'total_consultations': total_consultations,
        'total_appointments': total_appointments,
    }
    return render(request, 'dashboard/dashboard/dashboard.html', context)
