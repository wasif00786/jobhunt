from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('job',views.job,name='job'),
    path('seeker',views.seeker,name='seeker'),
    path('provider',views.provider,name='provider'),
    path('applied',views.applied,name='applied'),
    path('adcontact',views.adcontact,name='adcontact'),
]