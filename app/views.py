from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import Hospitals,Doctors,Departments,Home
from .forms import Appointment2Form,AppointmentForm,ContactForm

# Create your views here.

def home(request):
    dict_update={
        'latest_update':Home.objects.all()
    }
    return render(request,'home.html',dict_update)

def hospitals(request):
    dict_hospitals={
        'hos':Hospitals.objects.all()
    }
    return render(request,'hospitals.html',dict_hospitals)

def appointment(request):
    if request.method=='POST':
        form=AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form=AppointmentForm()
    dict_form={
        'app_form':form
    }
    return render(request,'appointment.html',dict_form)

def treatment(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'treatment.html',dict_dept)

def contact(request):
    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')

def doctors(request):
    dict_doctors={
        'doc':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_doctors)

def blog(request):
    return render(request,'blog.html')

def about(request):
    return render(request,'about.html')

def confirmation(request):
    return render(request,'confirmation.html')

def search_doctors(request):
    hospitals = Hospitals.objects.all()
    departments = Departments.objects.all()
    doctors = Doctors.objects.all()

    hospital_name = request.GET.get('hospital_name')
    department_name = request.GET.get('department_name')

    if hospital_name:
        doctors = doctors.filter(h_name__h_name=hospital_name)
    if department_name:
        doctors = doctors.filter(dept_name__dept_name=department_name)

    context = {
        'doctors': doctors,
        'hospitals': hospitals,
        'departments': departments
    }

    return render(request, 'doctors.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # Redirect to a success page after form submission
    form = ContactForm()
    dict_cont={'formm': form}
    return render(request, 'contact.html',dict_cont)


def appointment2(request):
    if request.method=='POST':
        form=Appointment2Form(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form=Appointment2Form()
    dict_form2={
        'a_form':form
    }
    return render(request,'appointment2.html',dict_form2)


def doctors_avail(request,pk):
    avail=Hospitals.objects.get(id=pk)

    return render(request,'doctors_avail.html',{"avail":avail,'form':form})