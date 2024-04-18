from django import forms
from .models import Feedback
'''class FeedbackForm(forms.Form):
    name = forms.CharField(required=True, error_messages={"required":"You forget to add your name",})
    rating = forms.IntegerField(min_value=1,max_value=5,widget=forms.Textarea)
    text = forms.CharField(label="Your feedback", widget=forms.Textarea, max_length=200)
    '''
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields ="__all__"
        exclude = ['product']
        