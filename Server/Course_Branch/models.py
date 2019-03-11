from django.db import models

# Create your models here.
class BRANCH(models.Model):
	branch_id = models.CharField(max_length=5, primary_key=True)
	branch_name = models.CharField(max_length=40)

class COURSE(models.Model):
	course_id = models.CharField(max_length=10, primary_key=True)
	course_name = models.CharField(max_length=40)
	branch = models.ForeignKey(BRANCH, related_name='courses', on_delete=models.CASCADE, null=False)