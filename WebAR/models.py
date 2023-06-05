from django.db import models
from django.core.validators import FileExtensionValidator  
from django.contrib.auth.models import User

class Image(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30)
    image = models.FileField(
        validators=[FileExtensionValidator(['gltf'])],
        upload_to='uploads/%Y/%m/%d/',
    )

    def __str__(self):
        return '<Owner:' + str(self.id) + ', ' + \
              'image:' + '(' + str(self.nickname) + ')>'
    

           
