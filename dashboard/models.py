from django.db import models
from django.utils.text import slugify

class Advice(models.Model):
	slug = models.SlugField(unique=True, blank=True, null=True)
	specialization = models.CharField(unique=True, max_length=50)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def  __str__(self):
		return self.specialization

	def save(self, *args, **kwargs):
		self.slug = slugify(self.specialization)
		super().save(*args, **kwargs)