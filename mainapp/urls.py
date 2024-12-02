from django.urls import path,include
from . import views
urlpatterns = [
    
    path('', views.index,name="index"),
    path('about', views.about,name="about"),
    path('services', views.services,name="services"),
    path('jobseekerreg', views.jobseekerreg,name="jobseekerreg"),
    path('provider', views.provider,name="provider"),
    path('logcode', views.logcode,name="logcode"),
    path('reg', views.reg,name="reg"),
    path('proreg', views.proreg,name="proreg"),
    path('contact', views.contact,name="contact"),
    path('adlogin', views.adlogin,name="adlogin"),
    path('logout', views.logout,name="logout"),
]