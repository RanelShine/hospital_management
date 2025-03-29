from django.shortcuts import render, get_object_or_404, redirect
from consultation.data.models import Consultation
from consultation.presentation.forms import ConsultationForm

def consultation_list(request):
    consultations = Consultation.objects.all()
    return render(request, 'consultation/consultation_list.html', {'consultations': consultations})

def consultation_detail(request, pk):
    consultation = get_object_or_404(Consultation, pk=pk)
    return render(request, 'consultation/consultation_detail.html', {'consultation': consultation})

def consultation_create(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            from consultation.business.services import create_consultation
            consultation = create_consultation(form.cleaned_data)
            return redirect('consultation_detail', pk=consultation.pk)
    else:
        form = ConsultationForm()
    return render(request, 'consultation/consultation_form.html', {'form': form})
