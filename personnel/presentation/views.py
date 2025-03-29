from django.shortcuts import render, get_object_or_404, redirect
from personnel.data.models import Personnel
from personnel.presentation.forms import PersonnelForm

def personnel_list(request):
    staff = Personnel.objects.all()
    return render(request, 'personnel/personnel_list.html', {'staff': staff})

def personnel_detail(request, pk):
    staff_member = get_object_or_404(Personnel, pk=pk)
    return render(request, 'personnel/personnel_detail.html', {'staff_member': staff_member})

def personnel_create(request):
    if request.method == 'POST':
        form = PersonnelForm(request.POST)
        if form.is_valid():
            from personnel.business.services import create_personnel
            personnel_obj = create_personnel(form.cleaned_data)
            return redirect('personnel_detail', pk=personnel_obj.pk)
    else:
        form = PersonnelForm()
    return render(request, 'personnel/personnel_form.html', {'form': form})
