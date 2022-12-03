from django import forms

class AddForm(forms.Form):
    a=forms.IntegerField(required=True)
    b=forms.IntegerField(required=True)