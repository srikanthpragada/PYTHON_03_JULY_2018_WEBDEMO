from django.forms import Form, CharField, BooleanField, Textarea, PasswordInput


class AddDeptForm(Form):
    deptname = CharField(max_length=20, label='Name')
    location = CharField(max_length=30, label='Location', initial='Mumbai')
    # feedback = CharField(label='Feedback', widget=Textarea)
    # onsite = BooleanField(label='On Site?')


class LoginForm(Form):
    username = CharField(max_length=10, label='Username')
    password = CharField(max_length=10, label='Password',
                         widget= PasswordInput)