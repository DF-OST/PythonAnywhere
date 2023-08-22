from django import forms

from .models import Meal

class PostForm(forms.ModelForm):

    class Meta:
        model = Meal
        fields = ('name', 'calorie_count', 'consumed_date')

class DateForm(forms.Form):
    thedate = forms.DateField(label="thedate")