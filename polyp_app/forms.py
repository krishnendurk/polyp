from django import forms
from polyp_app.models import *

class DatasetTableForm(forms.ModelForm):

    class Meta:
        model = DatasetTable
        fields = "__all__"

class DetectionTableForm(forms.ModelForm):

    class Meta:
        model = DetectionTable
        fields = "__all__"
