from django.db import models

# Create your models here.
class Doctor(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    nid = models.CharField(max_length=200, null=True)
    email = models.EmailField(blank=True, default="")
    password = models.CharField(max_length=200)
    conpassword = models.CharField(max_length=200)
    patient_address = models.CharField(max_length=100, null=True)
    contact_number = models.CharField(max_length=100, null=True)
    # bdate = models.DateTimeField(null=True, blank=True)
    age = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.first_name)


class Patient(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    nid = models.CharField(max_length=200, null=True)
    email = models.EmailField(blank=True, default="")
    password = models.CharField(max_length=200)
    conpassword = models.CharField(max_length=200)
    patient_address = models.CharField(max_length=100, null=True)
    contact_number = models.CharField(max_length=100, null=True)
    # bdate = models.DateTimeField(null=True, blank=True)
    age = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.first_name)


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    patientName = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=100, null=True)
    history = models.TextField(blank=True)
    date = models.DateTimeField(null=True)
    complication = models.TextField(blank=True)
    diagnosis = models.TextField(blank=True)
    advice = models.TextField(blank=True)
    due = models.CharField(max_length=200, default=0, null=True)
    dueLength = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.patientName)


class Dose(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, null=True)
    patientName = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(null=True)
    medicine = models.CharField(max_length=200, null=True)
    var1 = models.IntegerField(default=0, null=True)
    var2 = models.IntegerField(default=0, null=True)
    var3 = models.IntegerField(default=0, null=True)
    schedule = models.CharField(max_length=200, null=True)
    var4 = models.IntegerField(default=0, null=True)
    due = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.patientName)


class Pharmacy(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    pharmacy_reg_no = models.CharField(max_length=200, null=True)
    email = models.EmailField(blank=True, default="")
    password = models.CharField(max_length=200)
    conpassword = models.CharField(max_length=200)
    patient_address = models.CharField(max_length=100, null=True)
    contact_number = models.CharField(max_length=100, null=True)
    bdate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.first_name)


