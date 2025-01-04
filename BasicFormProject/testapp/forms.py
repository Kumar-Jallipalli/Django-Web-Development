from django import forms

## Form Class
class StudentForm (forms.Form):
    name = forms.CharField()
    marks = forms.IntegerField()