from django import forms

from video_lib.models import UploadModel


class UploadForm(forms.ModelForm):
    # file_name=forms.CharField(max_length=200)
    # file = forms.FileField(allow_empty_file=False)
    class Meta:
        model = UploadModel
        fields = '__all__'