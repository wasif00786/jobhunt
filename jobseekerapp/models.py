from django.db import models

# Create your models here.
class AppliedJobs(models.Model):
    id=models.AutoField(primary_key=True)
    empemailaddress=models.CharField(max_length=100,null=False)
    jobtitle=models.CharField(max_length=100)
    post=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.CharField(max_length=200)
    contactno=models.CharField(max_length=15)
    emailaddress=models.CharField(max_length=50)
    dob=models.CharField(max_length=30)
    qualification=models.CharField(max_length=100)
    experience=models.CharField(max_length=30)
    keyskills=models.CharField(max_length=200)
    applieddate=models.CharField(max_length=30) 

    def __str__(self) -> str:
        return self.jobtitle + " " + self.name