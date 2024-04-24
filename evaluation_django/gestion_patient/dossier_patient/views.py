from django.shortcuts import render # type: ignore
from .models import CentreDeSante, Praticien, Patient,tableau_Patient

def centre_de_sante_list(request):
    centres_de_sante = CentreDeSante.objects.all()
    return render(request, 'centre_de_sante_list.html', {'centres_de_sante': centres_de_sante})

def praticien_list(request):
    praticiens = Praticien.objects.all()
    return render(request, 'praticien_list.html', {'praticiens': praticiens})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})
 
def liste_patients(request):
    tableau_Patients =tableau_Patient.objects.all()
    return render(request,'liste_patients.html',{'tableau_Patients':tableau_Patients})


def index(request):
    return render(request, 'index.html')

