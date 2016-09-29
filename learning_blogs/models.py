from __future__ import unicode_literals

from django.db import models

class Topic(models.Model):
	'''A given topic a user wants to blog about'''
	text = models.CharField(max_length=100)
	date_uploaded = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text
