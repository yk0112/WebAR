from django import forms
from .models import Image
from django.contrib.auth.models import User

class AddImageForm(forms.ModelForm):
      #   def __init__(self, *args, **kwargs):
      #      super().__init__(*args, **kwargs)
      #      self.fields['owner'].widget.attrs['disabled'] = 'disabled'
        class Meta:
            model = Image
            fields = ['nickname','image']

class ImageSelectForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'] = forms.ChoiceField(
            choices=[(item.image, item.nickname) for item in Image.objects.filter(owner=user)]               
        )