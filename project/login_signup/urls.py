from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('doctor_reg', views.doctor_reg, name='doctor-reg'),
    path('pharmacy_reg', views.pharmacy_reg, name='pharmacy-reg'),
    path('home', views.home, name='home page'),
    path('pharmacy_home', views.pharmacy_home, name='pharmacy-home'),
    path('doctor_home', views.doctor_home, name='doctor-home'),
    path('prescription', views.prescription, name='prescription'),
    path('showPrescription/<prescriptionId>', views.showPrescription, name='/showPrescription'),
    path('allPrescription', views.allPrescription, name='all-prescription'),
    path('logout', views.logout, name='logout'),


    path('scanUser', views.scanUser, name='scanUser'),
    path('savePrescription/<pid>', views.savePrescription, name='savePrescription'),
]
