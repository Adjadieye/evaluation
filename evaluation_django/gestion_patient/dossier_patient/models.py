# models.py

from django.db import models

class CentreDeSante(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField()
    numero_telephone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nom

class Praticien(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)
    adresse_cabinet = models.TextField()
    numero_telephone = models.CharField(max_length=20)
    email = models.EmailField()
    centre_de_sante = models.ForeignKey(CentreDeSante, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Patient(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    adresse = models.TextField()
    numero_telephone = models.CharField(max_length=20)
    email = models.EmailField()
    dossier_medical = models.TextField()
    medecin_traitant = models.ForeignKey(Praticien, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class tableau_Patient(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    sexe = models.CharField(max_length=1, choices=[('M', 'Masculin'), ('F', 'Féminin')])
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nom} {self.prenom}"