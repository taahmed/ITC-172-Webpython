from django import forms
from .models import Tracks, RecordLabels, MediaType

# Basic forms are already tempated. 
# Forms can be customized

class TracksForm(forms.ModelForm):
    class Meta:
        model=Tracks
        fields='__all__'

class RecordLabelsForm(forms.ModelForm):
    class Meta:
        model=RecordLabels
        fields='__all__'

class MediaTypeForm(forms.ModelForm):
    class Meta:
        model=MediaType
        fields='__all__'