from django.forms import ModelForm
from .models import Cat


class CatList(ModelForm):
    class Meta:
        model = Cat
        fields = '__all__'
