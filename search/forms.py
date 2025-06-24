from django import forms

class SchoolSearchForm(forms.Form):
    location = forms.CharField(required=False)
    fee_min = forms.IntegerField(required=False)
    fee_max = forms.IntegerField(required=False)
    school_type = forms.CharField(required=False)
    facilities = forms.CharField(required=False)
    curriculum = forms.CharField(required=False)
    keywords = forms.CharField(required=False)
