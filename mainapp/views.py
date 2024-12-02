from django.shortcuts import render,redirect,reverse
from .models import Valid,Jobseeker,Employeer,Enquiry
from django.contrib import messages
import datetime
# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def jobseekerreg(request):
    return render(request , 'jobseekerreg.html')
def provider(request):
    return render(request , 'provider.html')
def adlogin(request):
    return render(request , 'adlogin.html')
def logout(request):
    try:
        if request.session['username']:
            del request.session['username']
            return redirect('mainapp:index')
        else:
            return redirect('mainapp:login')
    except:
        return redirect('mainapp:index')
def logcode(request):
    if request.method=='POST':
        user=request.POST['username']
        print(user)
        passw=request.POST['password']
        print(passw)
        usertype=request.POST['usertype']
        print(usertype)
        try:
            obj=Valid.objects.get(username=user,password=passw,usertype=usertype)
            if obj is not None:
                request.session['username']=user
                if  usertype == "ad":
                    request.session['usertype']="ad"
                    return redirect(reverse('adminapp:home'))
                elif  usertype == "provider":
                    request.session['usertype']="provider"
                    return redirect(reverse('jobprovider:proindex'))
                else:
                    return redirect(reverse('jobseeker:seekerindex'))
        except:
            messages.error(request, 'Invalid Credentials')
            if usertype == "ad":
                return redirect(reverse('mainapp:adlogin'))
            elif usertype == "provider":
                return redirect(reverse('mainapp:provider'))
            else:
                return redirect(reverse('mainapp:jobseekerreg'))
            
def reg(request):
    if request.method=='POST':
        name=request.POST['name']
        gender=request.POST['gender']
        address=request.POST['address']
        contact=request.POST['contactno']
        email=request.POST['email']
        password=request.POST['password']
        dob=request.POST['dob']
        qua=request.POST['qualification']
        exp=request.POST['experience']
        skill=request.POST['keyskill']
        seeker= Jobseeker(name=name,gender=gender,email=email,mobile=contact,address=address,qualification=qua,dob=dob,experience=exp,keyskills=skill)
        seeklog=Valid(username=email,password=password,usertype='jobseeker')
        seeker.save()
        seeklog.save()
    return redirect(reverse('mainapp:index'))
def proreg(request):
    if request.method=='POST':
        firmname=request.POST['firmname']
        firmwork=request.POST['firmwork']
        firmaddress=request.POST['firmaddress']
        cpname=request.POST['cpname']
        cpcontactno=request.POST['cpcontactno']
        cpemailaddress=request.POST['cpemailaddress']
        aadharno=request.POST['aadharno']
        panno=request.POST['panno']
        gstno=request.POST['gstno']
        password=request.POST['password']
        regdate=str(datetime.datetime.now()).split(' ')[0]
        provider=Employeer(firmname=firmname,firmwork=firmwork,firmaddress=firmaddress,cpname=cpname,cpcontactno=cpcontactno,cpemailaddress=cpemailaddress,aadharno=aadharno,panno=panno,gstno=gstno,regdate=regdate)
        prolog=Valid(username=cpemailaddress,password=password,usertype='provider')
        provider.save()
        prolog.save()
    return redirect(reverse('mainapp:index'))
def contact(request):
     if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        gender=request.POST['gender']
        mobile=request.POST['mobile']
        subject=request.POST['subject']
        msg=request.POST['message']
        regdate=datetime.date.today()
        enq=Enquiry(name=name,gender=gender,address=subject,contactno=mobile,emailid=email,enquirytext=msg,posteddate=regdate)
        enq.save()
        msg="Submitted"
        return redirect('mainapp:contact')
     else:
        return render(request , 'contact.html')
