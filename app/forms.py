from django import forms
from .models import Appointment2,Appointment,ContactMessage


class DateInput(forms.DateInput):
    input_type='date'

class Appointment2Form(forms.ModelForm):
    class Meta:
        model=Appointment2
        fields='__all__'

        widgets={
            'booking_date':DateInput()
        }

        labels={
            'pf_name':"First name",
            'pl_name':'Last name',
            'p_email':'Email',
            'doc_name':'Doctor Name',
           'booking_date':'Booking Date',
           'p_contact':'Contact No.',
           'p_country':'Country',
           'p_state':'state',
           'p_address':'Address',
           'p_purpose':'Purpose',
           'dept_name':'Department Name',
           'doc_name':'Doctor Name',
           'booking_date':'Appointment Date'

        }



class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields='__all__'

        labels={
            'pf_name':"First name",
            'pl_name':'Last name',
            'p_email':'Email',
            'doc_name':'Doctor Name',
           'booking_date':'Booking Date',
           'p_contact':'Contact No.',
           'p_country':'Country',
           'p_state':'state',
           'p_address':'Address',
           'p_purpose':'Purpose',
           'dept_name':'Department Name',
           'doc_name':'Doctor Name',
           'booking_date':'Appointment Date',
           'h_name':'Hospital Name'

        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = '__all__'