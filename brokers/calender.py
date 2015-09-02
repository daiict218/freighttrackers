mport datetime
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm, Form

class calender(forms.Form): 
  date_field = forms.DateField(widget=SelectDateWidget)