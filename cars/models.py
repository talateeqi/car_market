from django.db import models

class Car(models.Model):
	make = models.CharField(max_length=120)
	model = models.CharField(max_length=120)
	year = models.IntegerField()

	def __str__(self):
		return "{} {} - {}".format(self.make, self.model, self.year)