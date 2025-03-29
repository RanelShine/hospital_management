from django.shortcuts import render, get_object_or_404, redirect
from resources.data.models import Resource
from resources.presentation.forms import ResourceForm

def resource_list(request):
    resources = Resource.objects.all()
    return render(request, 'resources/resource_list.html', {'resources': resources})

def resource_detail(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    return render(request, 'resources/resource_detail.html', {'resource': resource})

def resource_create(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            from resources.business.services import create_resource
            resource = create_resource(form.cleaned_data)
            return redirect('resource_detail', pk=resource.pk)
    else:
        form = ResourceForm()
    return render(request, 'resources/resource_form.html', {'form': form})
