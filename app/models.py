from django.db import models

# Create your models here.
class Hospitals(models.Model):
    h_image=models.ImageField(upload_to='hospitals')
    h_name=models.CharField(max_length=200)
    h_description=models.TextField()
    h_contact=models.CharField(max_length=13)
    h_specialities=models.IntegerField()
    h_doctors=models.IntegerField()
    viewed_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.h_name 

class Departments(models.Model):
    dept_name=models.CharField(max_length=100)
    dept_description=models.TextField()

    def __str__(self):
        return self.dept_name 

class Doctors(models.Model):
    doc_name=models.CharField(max_length=200)
    doc_spec=models.CharField(max_length=200)
    dept_name=models.ForeignKey(Departments,on_delete=models.CASCADE, default=1)
    doc_image=models.ImageField(upload_to='doctors')
    h_name=models.ForeignKey(Hospitals,on_delete=models.CASCADE)

    def __str__(self):
        return 'Dr.' + self.doc_name + '-('+self.doc_spec+')'

class Appointment2(models.Model):
    pf_name=models.CharField(max_length=200)
    pl_name=models.CharField(max_length=200)
    p_email=models.EmailField()
    p_contact=models.CharField(max_length=10)
    p_country=models.CharField(max_length=100)
    p_state=models.CharField(max_length=100)
    p_address=models.TextField()
    p_purpose=models.TextField()
    dept_name=models.ForeignKey(Departments,on_delete=models.CASCADE)
    doc_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateTimeField(auto_now=True)

class Appointment(models.Model):
    pf_name=models.CharField(max_length=200)
    pl_name=models.CharField(max_length=200)
    p_email=models.EmailField()
    p_contact=models.CharField(max_length=10)
    p_country=models.CharField(max_length=100)
    p_state=models.CharField(max_length=100)
    p_address=models.TextField()
    p_purpose=models.TextField()
    h_name=models.ForeignKey(Hospitals,on_delete=models.CASCADE)
    dept_name=models.ForeignKey(Departments,on_delete=models.CASCADE)
    doc_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateTimeField(auto_now=True)

class Home(models.Model):
    latest_update=models.CharField(max_length=220)

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name