from django.forms import ModelForm
from .models import Booking

#Booking Form
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

