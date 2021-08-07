from django import forms
from app.models import CsvFile

class CsvFileForm(forms.ModelForm):
    class Meta:
        model = CsvFile
        fields = '__all__'