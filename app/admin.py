from django.contrib import admin
from .models import Hospitals,Departments,Doctors,Appointment,Appointment2,Home,ContactMessage

# Register your models here.

admin.site.register(Hospitals)
admin.site.register(Doctors)
admin.site.register(Departments)
admin.site.register(Home)


class Appointmentlist2(admin.ModelAdmin):
    list_display=('id','pf_name','pl_name','p_email','p_contact','p_country','p_state','p_address','p_purpose','dept_name','doc_name','booking_date','booked_on')

admin.site.register(Appointment2,Appointmentlist2)


class Appointmentlist(admin.ModelAdmin):
    list_display=('id','pf_name','pl_name','p_email','p_contact','p_country','p_state','p_address','p_purpose','dept_name','doc_name','h_name','booking_date','booked_on')

admin.site.register(Appointment,Appointmentlist)

admin.site.register(ContactMessage)