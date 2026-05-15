from django import forms
from .models import Fees

class FeesForm(forms.ModelForm):
    class Meta:
        model = Fees
        fields = '__all__'