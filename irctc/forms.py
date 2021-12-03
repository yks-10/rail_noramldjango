from django.forms import ModelForm
from .models import *
class Trainn(ModelForm):
    class Meta:
        model=Train
        fields=['train_name','train_no','train_starting','train_ending','timing']


class SearchForm(ModelForm):
    class Meta:
        model=Search
        fields=['train_starting','train_ending','timing']


class BookingForm(ModelForm):
    class Meta:
        model=Booking
        fields=['name','addhaar_no','count']
