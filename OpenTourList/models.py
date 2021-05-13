from django.db import models

class Recruit(models.Model):
	pass

class Item(models.Model):
	RecId = models.ForeignKey(Recruit, default=None, on_delete=models.CASCADE)
	text = models.TextField(default="")
