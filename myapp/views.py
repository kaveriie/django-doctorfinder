from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from random import randint
from django.core.mail import send_mail
import datetime


# Create your views here.

def home(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="doctor":
            return render(request,"myapp/dashboard/index.html",{'uid':uid})
        else:
            return render(request,"myapp/dashboard/indexpatient.html",{'uid':uid})

    else:
        return render(request,"myapp/home.html")


def login(request):
    return render(request,"myapp/authentication/login.html")

def register(request):
    return render(request,"myapp/authentication/register.html")

def registered(request):
    username=request.POST['username']
    email=request.POST['email']
    password=request.POST['password']
    role=request.POST['role']
    cid=User.objects.create(username=username,password=password,email=email,role=role)
    if role=="doctor":
        did=Doctor.objects.create(username=username,password=password,email=email)
    else:
        patientid=Patient.objects.create(username=username,password=password,email=email)

    subject="Confirmation Mail"
    msg="Welcome to DoctorFinder, "+str(username)
    send_mail(subject,msg,"k.kaveriie@gmail.com",[email])
    return render(request,"myapp/authentication/login.html")
    

def forgotpassword(request):
    return render(request,"myapp/authentication/forgot-password.html")



def index(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        did=Doctor.objects.get(d_id=uid)
        data=Doctor.objects.get(email=request.session['email'])
        alldocs=Doctor.objects.all()

        return render(request,"myapp/dashboard/index.html",{'uid':uid,'did':did,'data':data,'alldocs':alldocs})
    else:
        return render(request,"myapp/dashboard/index.html")

def indexpatient(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        return render(request,"myapp/dashboard/indexpatient.html",{'uid':uid})
    else:
        return render(request,"myapp/dashboard/indexpatient.html")




def bookappointment(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        return render(request,"myapp/appointment/book-appointment.html",{'uid':uid})
    else:
        return render(request,"myapp/appointment/book-appointment.html")
    




def adddoctor(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        data=Doctor.objects.get(email=request.session['email'])
        alldocs=Doctor.objects.all()

        return render(request,"myapp/doctor/add-doctor.html",{'uid':uid,'data':data,'alldocs':alldocs})
    else:
        return render(request,"myapp/doctor/add-doctor.html")

    

def doctors(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        data=Doctor.objects.get(email=request.session['email'])
        alldocs=Doctor.objects.all()

        return render(request,"myapp/doctor/doctors.html",{'uid':uid,'data':data,'alldocs':alldocs})
    else:
        return render(request,"myapp/doctor/doctors.html")


    

def events(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        data=Doctor.objects.get(email=request.session['email'])
        alldocs=Doctor.objects.all()

        return render(request,"myapp/doctor/events.html",{'uid':uid,'data':data,'alldocs':alldocs})
    else:
        return render(request,"myapp/doctor/events.html")


def doctorprofile(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        data=Doctor.objects.get(email=request.session['email'])
        alldocs=Doctor.objects.all()
        return render(request,"myapp/doctor/profile.html",{'uid':uid,'data':data,'alldocs':alldocs})
    else:
        return render(request,"myapp/doctor/profile.html")

    


def doctorsfp(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        return render(request,"myapp/doctor/doctors_forpatient.html",{'uid':uid})
    else:
        return render(request,"myapp/doctor/doctors_forpatient.html")

    
def eventsfp(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        return render(request,"myapp/doctor/events_forpatient.html",{'uid':uid})
    else:
        return render(request,"myapp/doctor/events_forpatient.html")


def profilefp(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        return render(request,"myapp/doctor/profile_forpatient.html",{'uid':uid})
    else:
        return render(request,"myapp/doctor/profile_forpatient.html")

    
def addpaymentfp(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        return render(request,"myapp/payment/addpaymentpatient.html",{'uid':uid})
    else:
        return render(request,"myapp/payment/addpaymentpatient.html")


def invoicefp(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        return HttpResponse("Under Construction")
    else:
        return HttpResponse("Under Construction")

    

def mypatientprofile(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        return render(request,"myapp/patients/mypatientprofile.html",{'uid':uid})
    else:
        return render(request,"myapp/patients/mypatientprofile.html")



def addpatients(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        did=Doctor.objects.get(d_id=uid)
        data=Doctor.objects.get(email=request.session['email'])
        alldocs=Doctor.objects.all()


        return render(request,"myapp/patients/add-patients.html",{'uid':uid,'did':did,'data':data,'alldocs':alldocs})
    else:
        return render(request,"myapp/patients/add-patients.html")


def allpatients(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        data=Doctor.objects.get(email=request.session['email'])
        alldocs=Doctor.objects.all()
        mypatients=Patient.objects.filter(doc_id=data)
        return render(request,"myapp/patients/all-patients.html",{'uid':uid,'data':data,'alldocs':alldocs,'mypatients':mypatients})
    else:
        return render(request,"myapp/patients/all-patients.html")
    
def invoice(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        return render(request,"myapp/patients/invoice.html",{'uid':uid})
    else:
        return render(request,"myapp/patients/invoice.html")

    
def patientsprofile(request,pk):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        pid=Patient.objects.get(id=pk)
        data=Doctor.objects.get(email=request.session['email'])
        alldocs=Doctor.objects.all()

        return render(request,"myapp/patients/patients-profile.html",{'uid':uid,'pid':pid,'data':data,'alldocs':alldocs})
    else:
        return render(request,"myapp/patients/patients-profile.html")



def addpayment(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        data=Doctor.objects.get(email=request.session['email'])
        alldocs=Doctor.objects.all()
        now = datetime.datetime.now()
        today=now.strftime("%Y-%m-%d")
        return render(request,"myapp/payment/add-payment.html",{'uid':uid,'data':data,'alldocs':alldocs,'today':today})
    else:
        return render(request,"myapp/payment/add-payment.html")

def allpayment(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        return render(request,"myapp/payment/all-payment.html",{'uid':uid})
    else:
        return render(request,"myapp/payment/all-payment.html")


def updatepayment(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])

    docid=request.POST['docid']
    patientid=request.POST['patientid']
    paymentno=request.POST['paymentno']
    patientname=request.POST['patientname']
    doctorname=request.POST['doctorname']
    paymentdate=request.POST['paymentdate']
    totalamount=request.POST['totalamount']
    paymentmethod=request.POST['paymentmethod']
    paymentstatus=request.POST['paymentstatus']

    print("****************************",paymentmethod,paymentstatus)

    doc_id=Doctor.objects.get(id=docid)
    patient_id=Patient.objects.get(id=patientid)

    paymentid=Payment.objects.create(doc_id=doc_id,patient_id=patient_id,paymentno=paymentno,patientname=patientname,doctorname=doctorname,paymentdate=paymentdate,totalamount=totalamount,paymentmethod=paymentmethod,paymentstatus=paymentstatus)
    paymentdata=Payment.objects.all()

    if paymentid:
        s_msg="Payment Added!"
        return render(request,"myapp/payment/add-payment.html",{'uid':uid,'paymentid':paymentid,'paymentdata':paymentdata,'s_msg':s_msg})
    else:
        e_msg="Sorry... There was an error adding payment, please try again!"
        return render(request,"myapp/payment/add-payment.html",{'e_msg':e_msg,'uid':uid})




def loginevaluate(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        currentuser=request.session['role']
        if currentuser=="patient":
            return render(request,"myapp/dashboard/indexpatient.html",{'uid':uid})        
        else:
            data=Doctor.objects.get(email=request.session['email'])
            alldocs=Doctor.objects.all()

            return render(request,"myapp/dashboard/index.html",{'uid':uid,'data':data,'alldocs':alldocs})
    else:
        try:
            uemail=request.POST['email']
            upassword=request.POST['password']
            uid=User.objects.filter(email=uemail)
            if uid:
                if uid[0].password==upassword:
                    s_msg="successfully login"
                    request.session['email']=uid[0].email
                    request.session['uid']=uid[0].id
                    request.session['username']=uid[0].username
                    request.session['role']=uid[0].role
                    currentuser=request.session['role']
                    if currentuser=="patient":
                        return render(request,"myapp/dashboard/indexpatient.html",{'uid':uid})
                    else:
                        data=Doctor.objects.get(email=request.session['email'])
                        alldocs=Doctor.objects.all()
                        return render(request,"myapp/dashboard/index.html",{'uid':uid,'data':data,'alldocs':alldocs})
                else:
                    e_msg="Invalid password"
                    return render(request,"myapp/authentication/login.html",{'e_msg':e_msg})
            else:
                e_msg="Invalid email"  
                return render(request,"myapp/authentication/login.html",{'e_msg':e_msg})
        except:
            e_msg="Invalid email or password" 
            return render(request,"myapp/authentication/login.html",{'e_msg':e_msg})



def logout(request):
    if "email" in request.session:
        del request.session['email']
        del request.session['uid']
        del request.session['username']
#        del request.session['role']
        
        s_msg="Succesfully logged out"
        return render(request,"myapp/authentication/login.html",{'s_msg':s_msg})
    else:
        return render(request,"myapp/authentication/login.html")
        



def viewuser(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        userdata=User.objects.all()
        data=Doctor.objects.get(email=request.session['email'])
        did=Doctor.objects.get(email=request.session['email'])
        alldocs=Doctor.objects.all()


        return render(request,"myapp/viewuser.html",{'uid':uid,'data':data,'did':did,'alldocs':alldocs,'userdata':userdata})
    else:
        return render(request,"myapp/viewuser.html")


def deleteuser(request,pk):
    uid=User.objects.get(id=pk)
    uid.delete()
    data=User.objects.all()
    return render(request,"myapp/viewuser.html",{'data':data})


def profileedit(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
    return render(request,"myapp/profileedit.html",{'uid':uid})


def profileupdate(request):
    if "profilepic" in request.FILES:
        id=request.POST['id']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        contactno=request.POST['contactno']
        profilepic=request.FILES['profilepic']

        uid=User.objects.get(id=id)
        uid.username=username
        uid.email=email
        uid.password=password
        uid.contactno=contactno
        uid.profilepic=profilepic
        uid.save()
        if uid.role == "patient":
            return render(request,"myapp/dashboard/indexpatient.html",{'uid':uid})
        else:
            return render(request,"myapp/dashboard/index.html",{'uid':uid})

    else:
        id=request.POST['id']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        contactno=request.POST['contactno']
        uid=User.objects.get(id=id)
        
        uid.username=username
        uid.email=email
        uid.password=password
        uid.contactno=contactno
        uid.save()
        if uid.role == "patient":
            return render(request,"myapp/dashboard/indexpatient.html",{'uid':uid})
        else:
            return render(request,"myapp/dashboard/index.html",{'uid':uid})
        

def sendotp(request):
    otp=randint(1111,9999)
    uid=User.objects.get(email=request.POST['email'])
    uid.otp=otp
    uid.save()
    msg="Your OTP is "+str(otp)
    send_mail("Forgot Password",msg,"k.kaveriie@gmail.com",[uid.email])
    return render(request,"myapp/authentication/resetpassword.html",{'uid':uid})

def resetpassword(request):
    email=request.POST['email']
    otp=request.POST['otp']
    newpassword=request.POST['newpassword']
    repassword=request.POST['repassword']
    uid=User.objects.get(email=email)

    if str(uid.otp)==str(otp):
        if newpassword==repassword:
            uid.password=newpassword
            uid.save()

            return render(request,"myapp/authentication/login.html")
        else:
            e_msg="Passwords do not match!"
            return render(request,"myapp/authentication/resetpassword.html",{'e_msg':e_msg,'uid':uid})

    else:
        e_msg="Invalid OTP"
        return render(request,"myapp/authentication/resetpassword.html",{'e_msg':e_msg,'uid':uid})







def imageupload(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        return render(request,"myapp/imageupload.html",{'uid':uid})
    else:
        return render(request,"myapp/imageupload.html")


def uploadimage(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])

    try:
        imgname=request.POST['imgname']
        img=request.FILES['img']
        gid=ImageGallery.objects.create(imgname=imgname,img=img)

        data=ImageGallery.objects.all()
        return render(request,"myapp/imagegallery.html",{'data':data,'uid':uid})        
    except:
        return render(request,"myapp/imageupload.html")

def imagegallery(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        imagedata=ImageGallery.objects.all()
        data=Doctor.objects.get(email=request.session['email'])
        alldocs=Doctor.objects.all()

        
        return render(request,"myapp/imagegallery.html",{'data':data,'uid':uid,'imagedata':imagedata,'alldocs':alldocs})
    else:
        return render(request,"myapp/imagegallery.html",{'data':data})




def audioupload(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        return render(request,"myapp/audioupload.html",{'uid':uid})
    else:
        return render(request,"myapp/audioupload.html")



def uploadaudio(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])

    try:
        songname=request.POST['songname']
        song=request.FILES['song']
        aid=AudioGallery.objects.create(songname=songname,song=song)

        data=AudioGallery.objects.all()
        return render(request,"myapp/audiogallery.html",{'data':data,'uid':uid})        

    except:
        return render(request,"myapp/audioupload.html")

def audiogallery(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        audiodata=AudioGallery.objects.all()
        data=Doctor.objects.get(email=request.session['email'])
        alldocs=Doctor.objects.all()

        return render(request,"myapp/audiogallery.html",{'data':data,'uid':uid,'audiodata':audiodata,'alldocs':alldocs})
    else:
        return render(request,"myapp/audiogallery.html",{'data':data})










def videoupload(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        return render(request,"myapp/videoupload.html",{'uid':uid})
    else:
        return render(request,"myapp/videoupload.html")



def uploadvideo(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])

    try:
        video=request.FILES['video']
        vid=VideoGallery.objects.create(video=video)

        data=VideoGallery.objects.all()
        return render(request,"myapp/videogallery.html",{'data':data,'uid':uid})        
    except:
        return render(request,"myapp/videoupload.html")

def videogallery(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        videodata=VideoGallery.objects.all()
        data=Doctor.objects.get(email=request.session['email'])
        alldocs=Doctor.objects.all()

        return render(request,"myapp/videogallery.html",{'data':data,'uid':uid,'videodata':videodata,'alldocs':alldocs})
    else:
        return render(request,"myapp/videogallery.html",{'data':data})

def askappointment(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])


    id=request.POST['id']
    fname=request.POST['fname']
    lname=request.POST['lname']
    dob=request.POST['dob']
    gender=request.POST['gender']
    service=request.POST['service']
    date=request.POST['date']
    email=request.POST['email']
    phoneno=request.POST['phoneno']
    message=request.POST['message']
    user_id=User.objects.get(id=id)


    bid=Booking.objects.create(p_id=user_id,fname=fname,lname=lname,dob=dob,gender=gender,service=service,date=date,email=email,phoneno=phoneno,message=message)
    data=Booking.objects.filter(p_id=uid)

    if data:
        s_msg="Your appointment has been booked!"
        return render(request,"myapp/myappointments.html",{'uid':uid,'bid':bid,'data':data,'s_msg':s_msg})
    else:
        e_msg="Sorry... There was an error booking your appointment, please try again!"
        return render(request,"myapp/appointment/book-appointment.html",{'e_msg':e_msg,'uid':uid})


def myappointments(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        data=Booking.objects.filter(p_id=uid)
        return render(request,"myapp/myappointments.html",{'data':data,'uid':uid})
    else:
        return render(request,"myapp/myappointments.html",{'data':data})


def myprofile(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        return render(request,"myapp/myprofile.html",{'uid':uid})
    else:
        return render(request,"myapp/myprofile.html")


def updatedoctor(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])


    fname=request.POST['fname']
    lname=request.POST['lname']
    dob=request.POST['dob']
    gender=request.POST['gender']
    service=request.POST['service']
    contactno=request.POST['contactno']
    username=request.POST['username']
    docemail=request.POST['email']
    password=request.POST['password']
    repassword=request.POST['repassword']

    if repassword!=password:
        errormsg="Passwords do not match!"
        return render(request,"myapp/doctor/add-doctor.html",{'errormsg':errormsg,'uid':uid})

    else:
        uid=User.objects.create(username=username,contactno=contactno,password=password,email=docemail,role="doctor")
        id=User.objects.get(email=docemail)
        did=Doctor.objects.create(d_id=id,fname=fname,lname=lname,dob=dob,gender=gender,service=service,contactno=contactno,username=username,email=docemail,password=password)
        data=Doctor.objects.get(email=docemail)

        if data:
            s_msg="Doctor Added!"
            return render(request,"myapp/doctor/add-doctor.html",{'uid':uid,'did':did,'data':data,'s_msg':s_msg})
        else:
            e_msg="Sorry... There was an error adding doctor, please try again!"
            return render(request,"myapp/doctor/add-doctor.html",{'e_msg':e_msg,'uid':uid})



def updatedocprofile(request):
    if "profilepic" in request.FILES:
        id=request.POST['id']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        contactno=request.POST['contactno']
        profilepic=request.FILES['profilepic']

        uid=User.objects.get(id=id)
        uid.username=username
        uid.email=email
        uid.password=password
        uid.contactno=contactno
        uid.profilepic=profilepic
        uid.save()

        fname=request.POST['fname']
        lname=request.POST['lname']
        docid=Doctor.objects.get(d_id=uid)
        docid.fname=fname
        docid.lname=lname
        docid.contactno=contactno
        docid.username=username
        docid.email=email
        docid.password=password

        docid.save()
        request.session['email']=uid.email

        data=Doctor.objects.get(email=request.session['email'])
        alldocs=Doctor.objects.all()

        return render(request,"myapp/doctor/profile.html",{'uid':uid,'data':data,'alldocs':alldocs,'docid':docid})

    else:
        id=request.POST['id']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        contactno=request.POST['contactno']
        uid=User.objects.get(id=id)
        
        uid.username=username
        uid.email=email
        uid.password=password
        uid.contactno=contactno
        uid.save()

        fname=request.POST['fname']
        lname=request.POST['lname']
        docid=Doctor.objects.get(d_id=uid)
        docid.fname=fname
        docid.lname=lname
        docid.contactno=contactno
        docid.username=username
        docid.email=email
        docid.password=password



        docid.save()
        request.session['email']=uid.email


        data=Doctor.objects.get(email=request.session['email'])
        alldocs=Doctor.objects.all()

        return render(request,"myapp/doctor/profile.html",{'uid':uid,'data':data,'alldocs':alldocs,'docid':docid})


def otherdocprofile(request,pk):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        did=Doctor.objects.get(id=pk)
        data=Doctor.objects.get(email=request.session['email'])
        alldocs=Doctor.objects.all()


        return render(request,"myapp/doctor/otherdocprofile.html",{'uid':uid,'did':did,'data':data,'alldocs':alldocs})
    else:            
        return render(request,"myapp/doctor/otherdocprofile.html")



def updatepatient(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])


    fname=request.POST['firstname']
    lname=request.POST['lastname']
    phoneno=request.POST['phoneno']
    service=request.POST['service']
    age=request.POST['age']
    gender=request.POST['gender']
    pemail=request.POST['email']
    description=request.POST['description']
    id=request.POST['id']
    datetime=request.POST['datetime']
    wardno=request.POST['wardno']
    username=pemail
    password=phoneno

    docid=Doctor.objects.get(id=id)


    patientid=Patient.objects.create(fname=fname,lname=lname,age=age,gender=gender,service=service,phoneno=phoneno,email=pemail,description=description,doc_id=docid,wardno=wardno,datetime=datetime,username=username,password=password)
    pdata=Patient.objects.all()

    mypatients=Patient.objects.filter(doc_id=docid)

    username=pemail
    email=pemail
    password=phoneno
    cid=User.objects.create(username=username,password=password,email=email,role="patient")




    if patientid:
        s_msg="Patient Added!"
        return render(request,"myapp/patients/all-patients.html",{'mypatients':mypatients,'uid':uid,'patientid':patientid,'pdata':pdata,'s_msg':s_msg})
    else:
        e_msg="Sorry... There was an error adding patient, please try again!"
        return render(request,"myapp/patients/all-patients.html",{'e_msg':e_msg,'uid':uid})



def docappointments(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        data=Doctor.objects.get(email=request.session['email'])
        did=Doctor.objects.get(email=request.session['email'])
        alldocs=Doctor.objects.all()
        aptmtdata=Booking.objects.all()

        
        
        #smsg n esmsg

        return render(request,"myapp/patients/docappointments.html",{'uid':uid,'data':data,'did':did,'alldocs':alldocs,'aptmtdata':aptmtdata})
    else:
        return render(request,"myapp/patients/docappointments.html")



def updatestatus(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        did=Doctor.objects.get(email=request.session['email'])
        data=Doctor.objects.get(email=request.session['email'])
        alldocs=Doctor.objects.all()
    
    
        id=request.POST['id']
        status=request.POST['status']


        oid=Booking.objects.get(id=id)
        oid.status=status
        oid.save()
        aptmtdata=Booking.objects.all()

        return render(request,"myapp/patients/docappointments.html",{'data':data,'uid':uid,'did':did,'alldocs':alldocs,'aptmtdata':aptmtdata,'oid':oid})



def dischargestatus(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        did=Doctor.objects.get(email=request.session['email'])
        data=Doctor.objects.get(email=request.session['email'])
        alldocs=Doctor.objects.all()
        mypatients=Patient.objects.filter(doc_id=data)

    
        id=request.POST['id']
        status=request.POST['status']


        pid=Patient.objects.get(id=id)
        pid.status=status
        pid.save()

        return render(request,"myapp/patients/all-patients.html",{'mypatients':mypatients,'data':data,'uid':uid,'did':did,'alldocs':alldocs,'pid':pid})


