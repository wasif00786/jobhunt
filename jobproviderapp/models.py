from django.db import models

# Create your models here.
class Jobs(models.Model):
    id=models.AutoField(primary_key = True)
    firmname=models.CharField(max_length=100)
    jobtitle=models.CharField(max_length=100)
    post=models.CharField(max_length=50)
    jobdesc=models.CharField(max_length=255)
    qualification=models.CharField(max_length=100)
    experience=models.CharField(max_length=20)
    location=models.CharField(max_length=100)
    salary=models.IntegerField()
    posteddate=models.CharField(max_length=30)
    emailaddress=models.CharField(max_length=60)
