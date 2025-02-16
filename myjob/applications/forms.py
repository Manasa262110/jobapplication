from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'resume', 'cover_letter']
    
    def clean_resume(self):
        """Ensure the uploaded file is a PDF."""
        resume = self.cleaned_data.get('resume')
        if resume and not resume.name.endswith('.pdf'):
            raise forms.ValidationError("Only PDF files are allowed.")
        return resume

    def clean_phone_number(self):
        """Ensure phone number is exactly 10 digits."""
        phone = self.cleaned_data.get('phone_number')
        if not phone.isdigit() or len(phone) != 10:
            raise forms.ValidationError("Phone number must be exactly 10 digits.")
        return phone
