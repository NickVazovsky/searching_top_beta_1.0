from  django import forms
from .models import SaveUrl
from .choices import *

class PostForm(forms.ModelForm):

    class Meta:
        model = SaveUrl
        exclude = [""]
