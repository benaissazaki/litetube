from django import forms


class VideoSearchForm(forms.Form):
    query = forms.CharField()
