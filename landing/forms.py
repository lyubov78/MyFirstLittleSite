from django import forms


class TemplateForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput)
    message = forms.CharField(widget=forms.Textarea)
