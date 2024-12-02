from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="seekerindex"),
    path('alljob',views.alljob,name="alljob"),
    path('applyjob/<int:id>',views.applyjob,name="applyjob"),
    path('contact',views.contact,name="contact"),
    path('appliedjob',views.appliedjob,name="appliedjob"),
    path('jobs/', views.job_list, name='job_list'),
]
