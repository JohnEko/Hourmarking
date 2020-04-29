from django.db import models


class Userhour(models.Model):
	first_name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=10)
	email = models.EmailField(max_length=30)
	userId = models.IntegerField(default=0)
	workTargetId = models.IntegerField(default=0)
	phoneNumber = models.IntegerField()
	isAdmin = models.BooleanField(default=True)
	dateTime = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.first_name+ " " +self.last_name










