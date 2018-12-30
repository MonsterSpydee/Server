from django.db import models
from Server.models import User
from Course_Branch.models import COURSE
from django.conf import settings
from FileUpload.models import File

# Create your models here.
class POST(models.Model):
	post_id = models.AutoField(primary_key=True) #AutoIncrement
	created_At = models.DateTimeField(auto_now_add=True)
	isNotes = models.BooleanField(default=True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE, null=False)
	course = models.ForeignKey(COURSE, related_name='posts', on_delete=models.CASCADE, null=False)
	num_upvotes = models.IntegerField(default=0)
	num_downvotes = models.IntegerField(default=0)
	num_views = models.IntegerField(default=0)
	content = models.ForeignKey(File, related_name='post', on_delete=models.CASCADE, null=False)

class VOTES_STATUS(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='statuses', on_delete=models.CASCADE, null=False)
	post = models.ForeignKey(POST, related_name='statuses', on_delete=models.CASCADE, null=False)
	status = models.IntegerField(default=0)