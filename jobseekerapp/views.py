from django.shortcuts import render,redirect,reverse
from . models import AppliedJobs
from jobproviderapp.models import Jobs 
from mainapp.models import Jobseeker , Employeer,Enquiry
from datetime import date
from django.db.models import Q
# Create your views here.
def index(request):
    try:
        if request.session['username']!=None:
            job=Jobs.objects.all()
            return render(request,'seekerindex.html',{'job':job})
    except:
        return redirect('mainapp:index')
def alljob(request):
    try:
        if request.session['username']!=None:
            job=Jobs.objects.all()
            return render(request,'seekerjobs.html',{'job':job})
    except:
        return redirect('mainapp:index')
def contact(request):
    try:
        if request.session['username']!=None:
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
                return redirect('jobseeker:contact')
            return render(request,'seekercontact.html')
    except:
        return redirect('mainapp:index')
def appliedjob(request):
    # try:
        if request.session['username']!=None:
            u=request.session['username']
            job=AppliedJobs.objects.filter(emailaddress=u)
            return render(request,'appliedjob.html',{'apjob':job})
        else:
            return redirect('mainapp:index')
    # except:
        return redirect('mainapp:index')
def applyjob(request,id):
    try:
        if request.session['username']!=None:
                u=request.session['username']
                user=Jobseeker.objects.get(email=u)
                j=Jobs.objects.get(id=id)
                empemailaddress=j.emailaddress
                jobtitle=j.jobtitle
                post=j.post
                name=user.name
                gender=user.gender
                address=j.location
                contactno=user.mobile
                emailaddress=user.email
                dob=user.dob
                qualification=user.qualification
                experience=user.experience
                keyskills=user.keyskills
                applieddate=date.today()
            # try:
                a=AppliedJobs.objects.filter(empemailaddress=empemailaddress,jobtitle=jobtitle,emailaddress=emailaddress)
                if a:
                    msg="Already Applied"
                    return redirect(reverse('jobseeker:alljob'),{'msg':msg})
                else:
                    apjob=AppliedJobs(empemailaddress=empemailaddress,jobtitle=jobtitle,post=post,name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,dob=dob,qualification=qualification,experience=experience,keyskills=keyskills,applieddate=applieddate)
                    apjob.save()
                    msg="Job Applied"
                    return redirect(reverse('jobseeker:alljob'),{'msg':msg})
            # except:
                return redirect(reverse('jobseeker:seekerindex'))      
    except:
        return redirect('mainapp:index') 
   

def job_list(request):
    query = request.GET.get('q', '')
    if query:
        job_list = Jobs.objects.filter(
            Q(firmname__icontains=query) |
            Q(jobtitle__icontains=query) |
            Q(post__icontains=query) |
            Q(jobdesc__icontains=query) |
            Q(qualification__icontains=query) |
            Q(experience__icontains=query) |
            Q(location__icontains=query) |
            Q(salary__icontains=query) |
            Q(posteddate__icontains=query) |
            Q(emailaddress__icontains=query)
        )
    else:
        job_list = Jobs.objects.all()

    context = {
        'job': job_list,
        'msg': f'Search results for "{query}"' if query else '',
    }
    return render(request, 'seekerjobs.html', context)