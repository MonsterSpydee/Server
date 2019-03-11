from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	total_upvotes_notes = models.IntegerField(default=0)
	total_downvotes_notes = models.IntegerField(default=0)
	total_upvotes_assignments = models.IntegerField(default=0)
	total_downvotes_assignments = models.IntegerField(default=0)
	branch = models.CharField(max_length=10)