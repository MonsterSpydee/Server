from django.db import models

# Create your models here.
class POINTS(models.Model):
	notes_upvote = models.IntegerField(default=5)
	notes_downvote = models.IntegerField(default=-2)
	assignments_upvote = models.IntegerField(default=10)
	assignments_downvote = models.IntegerField(default=-3)

