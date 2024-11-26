from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
	name = models.CharField(max_length=255, unique=True)
	description = models.TextField()
	address = models.CharField(max_length=255)
	phone_number = models.CharField(max_length=20)

	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name_plural = "Companies"


class Review(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	comment = models.TextField()
	rating = models.IntegerField()

	def save(self, *args, **kwargs):
		self.rating = min(max(self.rating, 1), 5)
		super(Review, self).save(*args, **kwargs)

	def __str__(self):
		return f"{self.user.username} - {self.company.name}"
	
	class Meta:
		unique_together = ('user', 'company')
