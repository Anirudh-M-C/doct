from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('hospitals/',views.hospitals,name="hospitals"),
    path('appointment/',views.appointment,name="appointment"),
    path('appointment2/',views.appointment2,name="appointment2"),
    path('treatment/',views.treatment,name="treatment"),
    path('contact/',views.contact,name="contact"),
    path('services/',views.services,name="services"),
    path('blog/',views.blog,name="blog"),
    path('about/',views.about,name="about"),
    path('doctors/',views.doctors,name="doctors"),
    path('confirmation/',views.confirmation,name="confirmation"),
    path('search_doctors/',views.search_doctors,name="search_doctors"),
    path('doctors_avail/<str:pk>/',views.doctors_avail,name="doctors_avail")
]
