from django import forms

# One Form = One Class

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(label="Proceed", required = False)