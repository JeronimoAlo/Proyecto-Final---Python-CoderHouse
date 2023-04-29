from django import forms
from AppPreEntreg3.models import choicesPant

class RemerasForm(forms.Form):
    id= forms.IntegerField()
    nombre= forms.CharField(max_length=30)
    tamaño = forms.CharField(max_length=3)
    color = forms.CharField(max_length=10)
    precio = forms.FloatField()
    stock = forms.IntegerField()

class BuzosForm(forms.Form):
    id= forms.IntegerField()
    nombre= forms.CharField(max_length=30)
    tamaño = forms.CharField(max_length=3)
    color = forms.CharField(max_length=10)
    precio = forms.FloatField()
    stock = forms.IntegerField()

class PantalonesForm(forms.Form):
    id= forms.IntegerField()
    nombre= forms.CharField(max_length=30)
    tamaño = forms.CharField(max_length=3)
    color = forms.CharField(max_length=10)
    diseño = forms.ChoiceField(choices=choicesPant)
    precio = forms.FloatField()
    stock = forms.IntegerField()