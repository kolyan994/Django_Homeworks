from django.db import models
from django.db.models import Model



class Sensor(Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=150, blank=True)

	def __str__(self):
		return self.name


class Measurement(Model):
	sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
	temperature = models.DecimalField(max_digits=5, decimal_places=2)
	measurement_date = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.sensor, self.temperature, self.measurement_date