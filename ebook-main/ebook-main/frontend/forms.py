from django.forms import ModelForm
from .models import Writings



class WritingForm(ModelForm):
    class Meta:
        model= Writings
        fields = "__all__"