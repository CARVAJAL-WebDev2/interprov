from django.db import models

class Tourist(models.Model):
	pass

class Item(models.Model):
	TourId = models.ForeignKey(Tourist, default=None, null=True, on_delete=models.CASCADE)
	text = models.TextField(default="")
	#pass