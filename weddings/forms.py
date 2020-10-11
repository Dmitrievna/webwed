from django.forms import ModelForm
from .models import Wedding

# a form class for a wedding

class WeddingForm(ModelForm):
    class Meta:
        model = Wedding
        fields = ['husband','wife','tasks','special_date','guests','suppliers']
