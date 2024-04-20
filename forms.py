from django import forms
from .models import Comment

class userforms(forms.Form):
    num1=forms.CharField(label='value1', max_length=20, required=False)
    num2=forms.CharField(label='value2', max_length=20, required=False)
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body' : forms.Textarea(attrs={'class':'form-control'})
        }