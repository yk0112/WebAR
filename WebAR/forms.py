from django import forms
from .models import Image
from django.contrib.auth.models import User


class AddImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["nickname", "image", "size"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["image"].widget.attrs.update(
            {"id": "add-file"}
        )
        self.fields["size"].widget.attrs.update(
            {"id": "default-size"}
        )


class ImageSelectForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["image1"] = forms.ChoiceField(
            choices=[
                (item.image, item.nickname) for item in Image.objects.filter(owner=user)
            ]
        )
        self.fields["image2"] = forms.ChoiceField(
            choices=[
                (item.image, item.nickname) for item in Image.objects.filter(owner=user)
            ]
        )
        self.fields["image3"] = forms.ChoiceField(
            choices=[
                (item.image, item.nickname) for item in Image.objects.filter(owner=user)
            ]
        )
        self.fields["image4"] = forms.ChoiceField(
            choices=[
                (item.image, item.nickname) for item in Image.objects.filter(owner=user)
            ]
        )
        self.fields["image5"] = forms.ChoiceField(
            choices=[
                (item.image, item.nickname) for item in Image.objects.filter(owner=user)
            ]
        )
