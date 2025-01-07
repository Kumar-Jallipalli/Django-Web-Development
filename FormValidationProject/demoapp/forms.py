from django import forms
from django.core import validators

def email_validator (value):
    if (value[-10:] != '@gmail.com' and value[-10:] != '@yahoo.com'):
        raise forms.ValidationError("Mail must end with '@gmail.com' or '@yahoo.com' ")

class EmployeeForm (forms.Form):
    ## 3. Form Validations with Custom Django Validators
    id = forms.IntegerField()
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    r_password = forms.CharField(label="Password (Again)", widget=forms.PasswordInput)
    email = forms.EmailField(validators=[email_validator])
    ## 2. Form Validations with inbuilt Django Validators
    feedback = forms.CharField(
        widget=forms.Textarea,
        validators=[
            validators.MinLengthValidator(10),
            validators.MaxLengthValidator(40)
        ]
    )
    bot_handler = forms.CharField(required=False, widget=forms.HiddenInput)

    ## 1. Form Validations with Sinle Clean function
    def clean_name(self):
        input_name = self.cleaned_data['name']
        if (input_name[0].lower() != 's' ):
            raise forms.ValidationError("Name must start with letter 's' ")
        return input_name
        
    def clean_id (self):
        id = self.cleaned_data['id']
        id = str(id)
        if (len(id) < 8):
            raise forms.ValidationError("Employee ID must be 8 digit")
        
    ## 4. Form Validations with multiple field validation together
    def clean(self):
        data = super().clean()
        pwd = data['password']
        r_pwd = data['r_password']
        if (pwd != r_pwd):
            raise forms.ValidationError("Passwors didn't match")


