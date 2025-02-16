from django.shortcuts import render, redirect
from .forms import JobApplicationForm
from django.contrib import messages

# Create your views here.
from django.shortcuts import render, redirect
from .forms import JobApplicationForm
from django.contrib import messages

def job_application_view(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your application has been submitted successfully!")
            return redirect('job_application')
    else:
        form = JobApplicationForm()
    
    return render(request, 'applications/job_application_form.html', {'form': form})
def home_view(request):
    return render(request, 'applications/home.html')
