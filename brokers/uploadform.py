from django import forms

class uploadform(forms.Form):
    f = forms.FileField(label='upload file')