from django.db import models

# Create your models here.
class Jobseeker(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False)
    gender=models.CharField(max_length=10) # True for male and False for female
    email = models.EmailField(unique=True)
    mobile = models.BigIntegerField()
    address = models.TextField()
    qualification = models.CharField(max_length=256)
    dob = models.CharField(max_length=256)
    experience = models.PositiveSmallIntegerField() 
    keyskills=models.CharField(max_length=256)
    regdate=models.DateTimeField(auto_now_add=True)
class Employeer(models.Model):
    id=models.AutoField(primary_key=True)
    firmname=models.CharField(max_length=100,null=False)
    firmwork=models.CharField(max_length=10)
    firmaddress = models.EmailField(unique=True)
    cpname=models.CharField(max_length=50)
    cpcontactno=models.BigIntegerField()
    cpemailaddress=models.EmailField(unique=True)
    aadharno=models.CharField(max_length=14)
    panno=models.CharField(max_length=10)
    gstno=models.CharField(max_length=15)
    regdate=models.CharField(max_length=30)
class Valid(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    usertype=models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.usertype   ## admin or employeer
                                                ## jobseeker
class Enquiry(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=6)
    address=models.CharField(max_length=255)
    contactno=models.BigIntegerField()
    emailid=models.EmailField()
    enquirytext=models.CharField(max_length=255)
    posteddate=models.CharField(max_length=30)
