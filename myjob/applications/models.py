from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Create your models here.

def validate_pdf(value):
    """Ensure uploaded file is a PDF."""
    if not value.name.endswith('.pdf'):
        raise ValidationError("Only PDF files are allowed.")

class JobApplication(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex=r'^\d{10}$', message="Phone number must be exactly 10 digits.")]
    )
    resume = models.FileField(upload_to='resumes/', validators=[validate_pdf])
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shortlisted', 'Shortlisted'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.status}"
