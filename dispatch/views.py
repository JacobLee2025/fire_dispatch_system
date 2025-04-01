from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import DispatchForm

def dispatch_form_view(request):
    if request.method == 'POST':
        form = DispatchForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            case_type = form.cleaned_data['case_type']
            return render(request, 'dispatch/result.html', {
                'location': location,
                'case_type': case_type,
            })
    else:
        form = DispatchForm()
    return render(request, 'dispatch/form.html', {'form': form})
