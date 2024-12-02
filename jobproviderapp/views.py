from django.shortcuts import render,redirect,reverse
from . models  import Jobs
from jobseekerapp.models import AppliedJobs
from mainapp.models import Jobseeker,Enquiry
from datetime import date
from django.contrib import messages
# Create your views here.
def index(request):
    try:
        if request.session['username'] and request.session['usertype']=="provider":
            emp=Jobseeker.objects.all()
            return render(request, 'proindex.html',{'emp':emp})
        else:
            return redirect('mainapp:index')
    except:
        return redirect('mainapp:index')
def addjob(request):
    try:
        if request.session['username'] and request.session['usertype']=="provider":
            return render(request,'addjob.html')
        else:
            return redirect('mainapp:index')
    except:
        return redirect('mainapp:index')
def procontact(request):
    try:
        if request.session['username'] and request.session['usertype']=="provider":
            if request.method=='POST':
                name=request.POST['name']
                email=request.POST['email']
                gender=request.POST['gender']
                mobile=request.POST['mobile']
                subject=request.POST['subject']
                msg=request.POST['message']
                regdate=date.today()
                enq=Enquiry(name=name,gender=gender,address=subject,contactno=mobile,emailid=email,enquirytext=msg,posteddate=regdate)
                enq.save()
                msg="Submitted"
                return redirect('provider:procontact')
            return render(request,'procontact.html')
        else:
            return redirect('mainapp:index')
    except:
        return redirect('mainapp:index')
def allseeker(request):
    try:
        if request.session['username'] and request.session['usertype']=="provider":
            emp=Jobseeker.objects.all()
            return render(request,'allseeker.html',{'emp':emp})
        else:
            return redirect('mainapp:index')
    except:
        return redirect('mainapp:index')
def appliedseeker(request):
    try:
        if request.session['username'] and request.session['usertype']=="provider":
            if request.session['username']:
                e=request.session['username']
                appjob=AppliedJobs.objects.filter(empemailaddress=e)
                return render(request,'appliedseeker.html',{'job':appjob,'e':e})
            else:
                return redirect('mainapp:index')
        else:
            return redirect('mainapp:index')
    except:
        return redirect('mainapp:index')
def addjobcode(request):
    # try:
        if request.session['username'] and request.session['usertype']=="provider":
            if request.method=='POST':
                firmname=request.POST['firmname']
                jobtitle=request.POST['jobtitle']
                post=request.POST['post']
                jobdesc=request.POST['jobdesc']
                qualification=request.POST['qualification']
                experience=request.POST['experience']
                location=request.POST['location']
                salary=request.POST['salary']
                posteddate=date.today()
                emailaddress=request.session.get('username')
                job=Jobs(firmname=firmname,jobtitle=jobtitle,post=post,jobdesc=jobdesc,qualification=qualification,experience=experience,location=location,salary=salary,posteddate=posteddate,emailaddress=emailaddress)
                job.save()
                return redirect(reverse('jobprovider:proindex'))
            else:
                return redirect(reverse('jobprovider:addjob'))
        else:
            return redirect('mainapp:index')


def alljob(request):
    username = request.session.get('username')
    if request.session['username'] and request.session['usertype']=="provider":
        job=Jobs.objects.filter(emailaddress=username)
        return render(request,'alljob.html',{'job':job})
    else:
        return redirect('mainapp:index')
    

def remove(request, id):
    obj = Jobs.objects.get(id=id)
    obj.delete()
    messages.success(request, 'Job Removed')
    return redirect(reverse('jobprovider:alljob'))