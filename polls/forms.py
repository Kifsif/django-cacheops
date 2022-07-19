from django import forms
from .models import Poll


class PollForm(forms.Form):
    poll = forms.ModelChoiceField(queryset=Poll.objects.all())
