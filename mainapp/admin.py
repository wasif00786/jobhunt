from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Jobseeker)
admin.site.register(Employeer)
admin.site.register(Enquiry)
admin.site.register(Valid)

