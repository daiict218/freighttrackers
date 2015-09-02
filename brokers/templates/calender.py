from django.contrib.admin.widgets import AdminDateWidget 

class myform(Form):
    my_field = DateField(widget = AdminDateWidget)