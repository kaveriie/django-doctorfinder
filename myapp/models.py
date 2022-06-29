from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    contactno=models.CharField(max_length=20,blank=True)
    USER_CHOICES = (
        ('d', 'doctor'),
        ('p', 'patient')
    )
    role = models.CharField(choices=USER_CHOICES, max_length=10,default='doctor')
    otp=models.IntegerField(default="123")
    profilepic=models.FileField(upload_to="myapp/img/",default="default.png")



class ImageGallery(models.Model):
    imgname=models.CharField(max_length=20)
    img=models.FileField(upload_to="myapp/img/",default="default.png")


class VideoGallery(models.Model):
    video=models.FileField(upload_to="myapp/videos/",null=True,verbose_name="")


class AudioGallery(models.Model):
    songname=models.CharField(max_length=20)
    song=models.FileField(upload_to="myapp/audio/")

class Booking(models.Model):
    p_id=models.ForeignKey(User,on_delete=models.CASCADE)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    service=models.CharField(max_length=30)
    date=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phoneno=models.CharField(max_length=20)
    message=models.CharField(max_length=200)
    status=models.CharField(max_length=20,default="Request Sent")


class Doctor(models.Model):
    d_id=models.ForeignKey(User,on_delete=models.CASCADE)
    fname=models.CharField(max_length=20,blank=True)
    lname=models.CharField(max_length=20,blank=True)
    dob=models.CharField(max_length=20,blank=True)
    gender=models.CharField(max_length=20,blank=True)
    service=models.CharField(max_length=20,blank=True)
    contactno=models.CharField(max_length=20,blank=True)
    username=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=30)



class Patient(models.Model):
    fname=models.CharField(max_length=20,blank=True)
    lname=models.CharField(max_length=20,blank=True)
    phoneno=models.CharField(max_length=20,blank=True)
    username=models.CharField(max_length=20,blank=True)
    password=models.CharField(max_length=20,blank=True)
    email=models.CharField(max_length=20,blank=True)
    service=models.CharField(max_length=20,blank=True)
    age=models.CharField(max_length=5,blank=True)
    gender=models.CharField(max_length=10,blank=True)
    email=models.CharField(max_length=30,blank=True)
    description=models.CharField(max_length=200,blank=True)
    doc_id=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    datetime=models.CharField(max_length=20,blank=True)
    wardno=models.CharField(max_length=10,blank=True)
    status=models.CharField(max_length=20,default="Confirmed")
    patientprofilepic=models.FileField(upload_to="myapp/img/",default="default.png")



class Payment(models.Model):
    doc_id=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient_id=models.ForeignKey(Patient,on_delete=models.CASCADE)
    paymentno=models.CharField(max_length=10,blank=True)
    patientname=models.CharField(max_length=20,blank=True)
    doctorname=models.CharField(max_length=20,blank=True)
    paymentdate=models.CharField(max_length=20,blank=True)
    totalamount=models.CharField(max_length=10,blank=True)
    paymentstatus=models.CharField(max_length=30,blank=True)
    paymentmethod=models.CharField(max_length=30,blank=True)