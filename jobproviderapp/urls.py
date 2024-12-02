from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='proindex'),
    path('addjob',views.addjob,name='addjob'),
    path('addjobcode',views.addjobcode,name='addjobcode'),
    path('procontact',views.procontact,name='procontact'),
    path('allseeker',views.allseeker,name='allseeker'),
    path('appliedseeker',views.appliedseeker,name='appliedseeker'),
    path('alljob/', views.alljob, name='alljob'),
    path('remove/<int:id>/', views.remove, name="remove"),
]