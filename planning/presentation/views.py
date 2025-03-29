from django.shortcuts import render, get_object_or_404, redirect
from planning.data.models import Appointment
from planning.presentation.forms import AppointmentForm

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'planning/appointment_list.html', {'appointments': appointments})

def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'planning/appointment_detail.html', {'appointment': appointment})

def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            from planning.business.services import create_appointment
            appointment = create_appointment(form.cleaned_data)
            return redirect('appointment_detail', pk=appointment.pk)
    else:
        form = AppointmentForm()
    return render(request, 'planning/appointment_form.html', {'form': form})
