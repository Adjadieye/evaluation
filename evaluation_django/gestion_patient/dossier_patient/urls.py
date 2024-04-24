from django.urls import path
from . import views

urlpatterns = [
    path('centres/', views.centre_de_sante_list, name='centre_de_sante_list'),
    path('praticiens/', views.praticien_list, name='praticien_list'),
    path('patients/', views.patient_list, name='patient_list'),
    path('tableau_patient/', views.liste_patients, name='liste_patients'),
    
    path('index/', views.index, name='index'),

]
