from django.db import models

# Create your models here.
class userImage(models.Model):
	the_image = models.ImageField(upload_to='media/images/', null=True)