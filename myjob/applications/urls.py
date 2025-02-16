from django.urls import path
from .views import job_application_view,  home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('apply/', job_application_view, name='job_application'),
]

