from django import forms
from .models import SchoolProfile, SchoolMedia, SchoolEvent

class SchoolProfileForm(forms.ModelForm):
    class Meta:
        model = SchoolProfile
        fields = '__all__'

class SchoolMediaForm(forms.ModelForm):
    class Meta:
        model = SchoolMedia
        fields = ['image', 'video', 'description']

class SchoolEventForm(forms.ModelForm):
    class Meta:
        model = SchoolEvent
        fields = ['title', 'description', 'date']
