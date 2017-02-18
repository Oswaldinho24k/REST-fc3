from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subject(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=200)

	def __str__(self):
		return self.title

class Course(models.Model):
	subject = models.ForeignKey(Subject, related_name='courses')
	alumni = models.ManyToManyField(User, related_name='courses')

	
