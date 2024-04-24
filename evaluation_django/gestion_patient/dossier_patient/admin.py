from django.contrib import admin
from .models import CentreDeSante, Patient, Praticien,tableau_Patient

admin.site.register(CentreDeSante)
admin.site.register(Patient)
admin.site.register(Praticien)
admin.site.register(tableau_Patient)