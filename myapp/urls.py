"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('index/', views.index, name='index'),
    path('indexpatient/', views.indexpatient, name='indexpatient'),
    path('registered/', views.registered, name='registered'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('resetpassword/', views.resetpassword, name='resetpassword'),
    path('sendotp/', views.sendotp, name='sendotp'),



    path('bookappointment/', views.bookappointment, name='bookappointment'),
    path('askappointment/', views.askappointment, name='askappointment'),
    path('myappointments/', views.myappointments, name='myappointments'),
    path('docappointments/', views.docappointments, name='docappointments'),


    path('updatestatus/', views.updatestatus, name='updatestatus'),
    path('dischargestatus/', views.dischargestatus, name='dischargestatus'),


    path('adddoctor/', views.adddoctor, name='adddoctor'),
    path('updatedoctor/', views.updatedoctor, name='updatedoctor'),

    path('doctors/', views.doctors, name='doctors'),
    path('doctorprofile/', views.doctorprofile, name='doctorprofile'),
    path('events/', views.events, name='events'),

    path('doctorsfp/', views.doctorsfp, name='doctorsfp'),
    path('eventsfp/', views.eventsfp, name='eventsfp'),
    path('profilefp/', views.profilefp, name='profilefp'),
    path('addpaymentfp/', views.addpaymentfp, name='addpaymentfp'),
    path('invoicefp/', views.invoicefp, name='invoicefp'),


    path('myprofile/', views.myprofile, name='myprofile'),
    path('otherdocprofile/<int:pk>', views.otherdocprofile, name='otherdocprofile'),


    path('addpatients/', views.addpatients, name='addpatients'),
    path('updatepatient/', views.updatepatient, name='updatepatient'),

    path('allpatients/', views.allpatients, name='allpatients'),
    path('patientsprofile/<int:pk>', views.patientsprofile, name='patientsprofile'),
    path('invoice/', views.invoice, name='invoice'),
    path('mypatientprofile/', views.mypatientprofile, name='mypatientprofile'),


    path('addpayment/', views.addpayment, name='addpayment'),
    path('allpayment/', views.allpayment, name='allpayment'),
    path('updatepayment/', views.updatepayment, name='updatepayment'),



    path('loginevaluate/', views.loginevaluate, name='loginevaluate'),
    path('logout/', views.logout, name='logout'),

    path('viewuser/', views.viewuser, name='viewuser'),
    path('deleteuser/<int:pk>', views.deleteuser, name='deleteuser'),

    path('profileedit/', views.profileedit, name='profileedit'),
    path('profileupdate/', views.profileupdate, name='profileupdate'),

    path('updatedocprofile/', views.updatedocprofile, name='updatedocprofile'),


    path('imageupload/', views.imageupload, name='imageupload'),
    path('uploadimage/', views.uploadimage, name='uploadimage'),
    path('imagegallery/', views.imagegallery, name='imagegallery'),



    path('videoupload/', views.videoupload, name='videoupload'),
    path('uploadvideo/', views.uploadvideo, name='uploadvideo'),
    path('videogallery/', views.videogallery, name='videogallery'),


    path('audioupload/', views.audioupload, name='audioupload'),
    path('uploadaudio/', views.uploadaudio, name='uploadaudio'),
    path('audiogallery/', views.audiogallery, name='audiogallery'),

]
