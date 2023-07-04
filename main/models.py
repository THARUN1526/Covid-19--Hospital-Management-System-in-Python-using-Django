from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=15)
    patient_relative_name = models.CharField(max_length=50, null=True)
    patient_relative_contact = models.CharField(max_length=15, null=True)
    address = models.TextField()
    SYMPTOMS = (
        ('Fever', 'Fever'),
        ('Dry cough', 'Dry cough'),
        ('Tiredness', 'Tiredness'),
        ('Aches and pains', 'Aches and pains'),
        ('Sore throat', 'Sore throat'),
        ('Diarrhoea', 'Diarrhoea'),
        ('Loss of taste or smell', 'Loss of taste or smell'),
        ('Difficulty in breathing or shortness of breath', 'Difficulty in breathing or shortness of breath'),
        ('Chest pain or pressure', 'Chest pain or pressure'),
        ('Loss of speech or movement', 'Loss of speech or movement'),
    )

    symptoms = MultiSelectField(choices=SYMPTOMS, null=True)
    prior_ailments = models.TextField()
    bed_num = models.ForeignKey("Bed", on_delete=models.CASCADE)
    dob = models.DateField(null=True)
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE, null=True)
    doctors_notes = models.TextField(null=True, blank=True)
    doctors_visiting_time = models.CharField(null=True, max_length=50, blank=True)
    status = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
        
class Bed(models.Model):
    bed_number = models.CharField(max_length=50)
    occupied = models.BooleanField()
    def __str__(self):
        return self.bed_number


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name




