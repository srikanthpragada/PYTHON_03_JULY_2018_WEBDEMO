from django.forms import Form, CharField


class AddDeptForm(Form):
    deptname = CharField(max_length=20, label='Name')
    location = CharField(max_length=30, label='Location')
