from django.db import models


class Airports(models.Model):
	code = models.CharField(max_length=3)
	city = models.CharField(max_length=64)
	def __str__(self):
		return f"{self.city}({self.code})"


class Flight(models.Model):
	origin = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name="depatures")
	destination = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name="arrivals")
	duration = models.IntegerField()
	def  __str__(self):
		return f"{self.id}:{self.origin} to {self.destination}"


	def is_valid_flight(self):
		return self.origin != self.destination and self.duration > 0
		


class Passengers(models.Model):
	first = models.CharField(max_length=64)
	last = models.CharField(max_length=64)
	flights = models.ManyToManyField(Flight, blank=True, related_name="passenegers")

	def __str__(self):
		return f"{self.first} {self.last}"





# class Flight(models.Model):
# 	origin = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name="depatures")
# 	destination = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name="arrivals")
# 	duration = models.IntegerField()
# 	def  __str__(self):
# 		return f"{self.id}:{self.origin} to {self.destination}"
