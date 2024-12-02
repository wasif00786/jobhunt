from django.shortcuts import render,redirect,reverse
from jobseekerapp.models import AppliedJobs
from jobproviderapp.models import *
from mainapp.models import *
# Create your views here.
def index(request):
    # try:
        if request.session['username'] and request.session['usertype']=='ad':
            aj=len(AppliedJobs.objects.all())
            job=len(Jobs.objects.all())
            seeker=len(Jobseeker.objects.all())
            emp=len(Employeer.objects.all())
            return  render(request, 'adindex.html',locals())
        else:
            return  redirect('mainapp:index')
    # except:
        return redirect('mainapp:index')
def job(request):
    try:
        if request.session['username'] and request.session['usertype']=='ad':
            job=Jobs.objects.all()
            return  render(request, 'adjob.html',locals())
        else:
            return  redirect('mainapp:index')
    except:
        return redirect('mainapp:index')
def seeker(request):
    try:
        if request.session['username'] and request.session['usertype']=='ad':
            seeker=Jobseeker.objects.all()
            return  render(request, 'adseeker.html',locals())
        else:
            return  redirect('mainapp:index')
    except:
        return redirect('mainapp:index')
def provider(request):
    # try:
        if request.session['username'] and request.session['usertype']=='ad':
            provider=Employeer.objects.all()
            return  render(request, 'adprovider.html',locals())
        else:
            return  redirect('mainapp:index')
    # except:
        return redirect('mainapp:index')
def applied(request):
    try:
        if request.session['username'] and request.session['usertype']=='ad':
            aj=AppliedJobs.objects.all()
            return  render(request, 'adapplied.html',locals())
        else:
            return  redirect('mainapp:index')
    except:
        return redirect('mainapp:index')
def adcontact(request):
    # try:
        if request.session['username'] and request.session['usertype']=='ad':
            enq=Enquiry.objects.all()
            v=Valid.objects.values_list('username')
            
            return  render(request, 'adcontact.html',locals())
        else:
            return  redirect('mainapp:index')
    # except:
        return redirect('mainapp:index')
    