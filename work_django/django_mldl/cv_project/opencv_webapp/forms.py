from django import forms
<<<<<<< Updated upstream
=======
from .models import ImageUploadModel
>>>>>>> Stashed changes

class SimpleUploadForm(forms.Form):
    title = forms.CharField(max_length=50)
    # ImageField Inherits all attributes and methods from FileField, but also validates that the uploaded object is a valid image.
    # file = forms.FileField()
    image = forms.ImageField()
<<<<<<< Updated upstream
=======


class ImageUploadForm(forms.ModelForm):

    # ImageUploadModel에 있는 열 중에 받아드리고 싶은 열만 fields로 가져옴
    class Meta:
        model = ImageUploadModel
        fields = ('description', 'document')
>>>>>>> Stashed changes
