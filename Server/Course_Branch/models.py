from django.db import models

# Create your models here.
class BRANCH(models.Model):
	branch_id = models.CharField(max_length=5, unique=True)
	branch_name = models.CharField(max_length=40, unique=True)

class COURSE(models.Model):
	course_id = models.CharField(max_length=10, unique=True)
	course_name = models.CharField(max_length=40)
	branch = models.ForeignKey(BRANCH, related_name='courses', on_delete=models.CASCADE, null=False)