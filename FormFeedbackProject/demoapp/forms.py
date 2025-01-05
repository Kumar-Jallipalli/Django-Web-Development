from django import forms

class FeedbackForm (forms.Form):
    name = forms.CharField()
    roll_no = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)