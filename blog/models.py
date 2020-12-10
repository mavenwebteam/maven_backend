from django.db import models
from ckeditor.fields import RichTextField



class Post(models.Model):
	title = models.CharField(max_length=255)
	content = RichTextField(blank=True, null=True)
	content_type = models.CharField(max_length=255)
	date = models.DateField()

	def __str__(self):
		return self.title 


class Profile(models.Model):
	name = models.CharField(max_length=255)
	role = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)
	email = models.EmailField()
	address = RichTextField(blank=True, null=True)

	def __str__(self):
		return '{}'.format(self.name)


class Record(models.Model):
	name = models.ForeignKey(Profile, on_delete=models.CASCADE)
	intime = models.CharField(max_length=255, default='10:00 AM')
	outtime = models.CharField(max_length=255, default='05:00 PM')
	kpi = RichTextField(blank=True, null=True)
	absent = models.BooleanField(default=False)
	date = models.DateField()
