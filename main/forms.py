from django import forms
from .models import *

#add business form
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('name', 'location', 'image')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('comment', 'rating')