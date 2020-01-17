from django.db import models

# Create your models here.
class Visitor(models.Model):
	the_image = models.ImageField(upload_to='media/images/', null=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	def __str__(self):
		return (self.first_name + self.last_name)

	def delete(self, *args, **kwargs):
		self.the_image.delete()
		super().delete(*args, **kwargs)