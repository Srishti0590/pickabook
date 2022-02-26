from django.db import models
from django.db import models
from django.core.validators import *
from django.core import validators
# Create your models here.
class Writings(models.Model):
    objects = None
    topic = models.CharField( max_length=500, null=True)
    story = models.TextField(null=True)
    image = models.FileField(upload_to='static/uploads', null=True)
    name= models.CharField(max_length=500, null=True, validators=[validators.MinLengthValidator(2)])
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.topic