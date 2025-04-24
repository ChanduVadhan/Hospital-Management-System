from django.shortcuts import render, redirect
from django.contrib import messages
from base.models import HealthForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Home View
@login_required(login_url='login_')
def home(request):
    query = request.GET.get('q', '').strip()  # Get the search query

    if query:
        all_data = HealthForm.objects.filter(
            Q(full_name__icontains=query) |
            Q(phone__icontains=query) |
            Q(address__icontains=query) |
            Q(age__icontains=query) |
            Q(gender__icontains=query) |
            Q(state__icontains=query) |
            Q(aadhaar_number__icontains=query) |
            Q(email__icontains=query) |
            Q(health_problem__icontains=query)
        )
    else:
        all_data = []

    return render(request, 'home.html', {'all_data': all_data, 'query': query})

# Health Form View
def health_form_view(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        address = request.POST['address']
        age = request.POST['age']
        gender = request.POST['gender']
        state = request.POST['state']
        aadhaar_number = request.POST['aadhaar']
        email = request.POST['email']
        health_problem = request.POST['health_problem']

        HealthForm.objects.create(
            full_name=full_name,
            phone=phone,
            address=address,
            age=age,
            gender=gender,
            state=state,
            aadhaar_number=aadhaar_number,
            email=email,
            health_problem=health_problem
        )
        messages.success(request, "Form submitted successfully!")

    return render(request, 'health_form.html')

# Display Patients' Records
def patients_record(request):
    records = HealthForm.objects.all()
    return render(request, 'patients.html', {'data': records})

# Edit Patient View
def edit_patient(request, id):
    patient = HealthForm.objects.get(id=id)


    if request.method == "POST":
        patient.full_name = request.POST['full_name']
        patient.phone = request.POST['phone']
        patient.address = request.POST['address']
        patient.age = request.POST['age']
        patient.gender = request.POST['gender']
        patient.state = request.POST['state']
        patient.aadhaar_number = request.POST['aadhaar']
        patient.email = request.POST['email']
        patient.health_problem = request.POST['health_problem']
        
        patient.save()
        return redirect('patients_record')  

    return render(request, 'edit_patient.html', {"patient": patient})  



def delete_record(request, id):
    patient = HealthForm.objects.get(id=id)

    if request.method == "POST":
        patient.delete()
        return redirect("patients_record")  

    return render(request, "delete_record.html", {"patient": patient})


def patient_details(request, id):
    patient =  HealthForm.objects.get(id=id)
    return render(request, 'patient_details.html', {'patient': patient})



