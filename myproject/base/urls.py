from django.urls import path
from base import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('patient_registration/', views.health_form_view, name='patient_registration'),
    path('patients_record/', views.patients_record, name='patients_record'), 
    path('edit/<int:id>/', views.edit_patient, name='edit'),  
    path("delete/<int:id>/", views.delete_record, name="delete_record"),
    path('details/<int:id>/', views.patient_details, name='patient_details'),
  
]
