from django.forms import ModelForm
from .models import FormatMaterial

class FormatMaterialForm(ModelForm):
    class Meta:
        model = FormatMaterial
        fields = ['format', 'material']