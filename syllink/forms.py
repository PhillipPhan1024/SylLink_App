from django import forms
from .models import SyllabusUploader

class SyllabusUploaderForm(forms.ModelForm):
    class Meta:
        model = SyllabusUploader
        fields = ('description', 'syllabus', )