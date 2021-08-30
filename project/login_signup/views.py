from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import Group
from django.contrib import messages
from django.http import HttpResponse
from .models import Patient, Doctor, Pharmacy, Prescription, Dose
from .decorators import unauthenticated_user, allowed_users, user_only, patient_only, pharmacy_only


# from .models import user


# Create your views here.
@patient_only
@allowed_users(allowed_roles=['patient'])
def home(request):
    return render(request, 'home.html')


@user_only
def doctor_home(request):
    return render(request, 'doctor_dashboard.html')


@user_only
def prescription(request):
    user = User.objects.all()
    return render(request, 'users.html', {'user': user})


@user_only
def showPrescription(request, prescriptionId):
    prescription = Prescription.objects.get(id=prescriptionId)
    dose = Dose.objects.filter(prescription=prescription)
    return render(request, 'patientsPrescription.html', {'prescription': prescription, 'dose': dose})


@user_only
def allPrescription(request):
    doctorName = request.user.username
    doctor = Doctor.objects.get(first_name=doctorName)
    allPrescriptions = Prescription.objects.filter(doctor=doctor)
    due_date = datetime.now().date() - timedelta(days=30)
    thisMonthPrescriptions = Prescription.objects.filter(doctor=doctor, date__gt=due_date)
    return render(request, 'allPrescription.html', {'prescriptions': allPrescriptions, 'thisMonthPrescriptions': thisMonthPrescriptions})


@user_only
def scanUser(request):
    if request.method == 'POST':
        userID = request.POST['userID']
        patient = User.objects.get(pk=userID)
        patientInfo = Patient.objects.get(first_name=patient.username)
        date = datetime.now().date()
        print(date)
    return render(request, 'prescription.html', {'patient': patientInfo, 'date': date, 'pID': userID})


@user_only
def savePrescription(request, pid):
    doctor_id = request.user.username
    doctor = Doctor.objects.get(first_name=doctor_id)
    patient = User.objects.get(pk=pid)
    patientInfo = Patient.objects.get(first_name=patient.username)
    date = datetime.now().date()

    if request.method == 'POST':
        history = request.POST['history']
        complication = request.POST['complication']
        diagnosis = request.POST['diagnosis']
        advice = request.POST['advice']
        gender = request.POST['gender']
        due = request.POST['due']
        dueLength = request.POST['dueLength']
        print("hello")

        pres_table = Prescription(patient=patientInfo, doctor=doctor, patientName=patientInfo.first_name,
                                  phone=patientInfo.contact_number, date=date, history=history,
                                  complication=complication, diagnosis=diagnosis, advice=advice, due=due,
                                  dueLength=dueLength, gender=gender)
        pres_table.save()

        medicine1 = request.POST['med1']
        var1 = request.POST['var1']
        var2 = request.POST['var2']
        var3 = request.POST['var3']
        schedule = request.POST['schedule']
        var4 = request.POST['var4']
        dueType = request.POST['dueType']

        med1 = Dose(patient=patientInfo, doctor=doctor, date=date, prescription=pres_table, patientName=patientInfo,
                    medicine=medicine1, var1=var1, var2=var2, var3=var3, schedule=schedule, var4=var4, due=dueType)
        med1.save()

        medicine2 = request.POST['med2']
        var12 = request.POST['var12']
        var22 = request.POST['var22']
        var32 = request.POST['var32']
        schedule2 = request.POST['schedule2']
        var42 = request.POST['var42']
        dueType2 = request.POST['due2']

        med2 = Dose(patient=patientInfo, doctor=doctor, date=date, prescription=pres_table, patientName=patientInfo,
                    medicine=medicine2, var1=var12, var2=var22, var3=var32, schedule=schedule2, var4=var42,
                    due=dueType2)
        med2.save()

        medicine3 = request.POST['med3']
        var13 = request.POST['var13']
        var23 = request.POST['var23']
        var33 = request.POST['var33']
        schedule3 = request.POST['schedule3']
        var43 = request.POST['var43']
        dueType3 = request.POST['due3']

        med13 = Dose(patient=patientInfo, doctor=doctor, date=date, prescription=pres_table, patientName=patientInfo,
                     medicine=medicine3, var1=var13, var2=var23, var3=var33, schedule=schedule3, var4=var43,
                     due=dueType3)
        med13.save()
    return redirect('doctor-home')


@pharmacy_only
@allowed_users(allowed_roles=['pharmacy'])
def pharmacy_home(request):
    return render(request, 'pharmacy_home.html')


def login(request):
    if request.method == 'POST':
        # email = request.POST['email']
        # password = request.POST['password']
        usernameOrEmail = request.POST['username']

        try:
            username = User.objects.get(email=usernameOrEmail).username
        except User.DoesNotExist:
            username = request.POST['username']
        password = request.POST['password']

        # reg_user = auth.authenticate(username=username,email=email,password=password)
        reg_user = auth.authenticate(username=username, password=password)

        if reg_user is not None:
            auth.login(request, reg_user)
            return redirect(home)
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        nid = request.POST['nid']
        email = request.POST['email']
        password = request.POST['password']
        conpassword = request.POST['conpassword']
        address = request.POST['address']
        contact = request.POST['contact']
        bdate = request.POST['date']

        patient = Patient(first_name=firstname, last_name=lastname, nid=nid, email=email, password=password,
                          conpassword=conpassword, patient_address=address, contact_number=contact, age=bdate)

        if password == conpassword:
            if Patient.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            if Patient.objects.filter(nid=nid).exists():
                messages.info(request, 'NID already exist')
                return redirect('register')
            if Patient.objects.filter(first_name=firstname).exists():
                messages.info(request, 'User already exist')
                return redirect('register')

            else:
                reg_user = User.objects.create_user(username=firstname, email=email, password=password)
                reg_user.save()
                patient.save()

                group = Group.objects.get(name='patient')
                reg_user.groups.add(group)

                messages.info(request, 'User created')

                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')

    return render(request, "register.html")


def doctor_reg(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        nid = request.POST['number']
        email = request.POST['email']
        password = request.POST['password']
        conpassword = request.POST['conpassword']
        address = request.POST['address']
        contact = request.POST['contact']
        bdate = request.POST['date']

        doctor = Doctor(first_name=firstname, last_name=lastname, nid=nid, email=email, password=password,
                        conpassword=conpassword, patient_address=address, contact_number=contact, age=bdate)

        if password == conpassword:
            if Doctor.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('doctor-reg')
            if Doctor.objects.filter(nid=nid).exists():
                messages.info(request, 'NID already exist')
                return redirect('doctor-reg')

            else:
                reg_user = User.objects.create_user(username=firstname, email=email, password=password)

                group = Group.objects.get(name='doctor')
                reg_user.groups.add(group)
                reg_user.save()
                doctor.save()

                messages.info(request, 'User created')

                return redirect('login')

        else:
            messages.info(request, 'Password not matching')
            return redirect('doctor-reg')
    return render(request, "doctor_registration.html")


def pharmacy_reg(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        pharmacy_reg_no = request.POST['number']
        email = request.POST['email']
        password = request.POST['password']
        conpassword = request.POST['conpassword']
        address = request.POST['address']
        contact = request.POST['contact']
        bdate = request.POST['date']

        pharmacy = Pharmacy(first_name=firstname, last_name=lastname, pharmacy_reg_no=pharmacy_reg_no, email=email,
                            password=password, conpassword=conpassword, patient_address=address, contact_number=contact,
                            bdate=bdate)

        if password == conpassword:
            if Pharmacy.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('pharmacy_reg')
            if Pharmacy.objects.filter(pharmacy_reg_no=pharmacy_reg_no).exists():
                messages.info(request, 'Registration number already exist')
                return redirect('pharmacy_reg')

            else:
                reg_user = User.objects.create_user(username=firstname, email=email, password=password)
                reg_user.save()
                pharmacy.save()

                group = Group.objects.get(name='pharmacy')
                reg_user.groups.add(group)

                messages.info(request, 'User created')

                return redirect('login')

        else:
            messages.info(request, 'Password not matching')
            return redirect('pharmacy_reg')
    return render(request, "pharmacy_reg.html")


def logout(request):
    auth.logout(request)
    return redirect('login')
