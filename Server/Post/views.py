from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from rest_framework import status
from Server.models import User
from Course_Branch.models import COURSE
from .models import POST
from Course_Branch.models import BRANCH

class upvoteView(APIView):
	def get(self, request):
		pass

	def post(self,request,format = 'json'):
		# User.objects.create(username="barry_19281", password="barry_19281", 
		# 	first_name="rajat")
		author = User.objects.get(username="barry_19281",password="barry_19281")

		# User.objects.create(username="pratikshya361", password="pratikshya361",
		# 	first_name="pratikshya")
		

		# branch = BRANCH.objects.get(branch_id="CSE")
		# course = COURSE.objects.get(course_id="CSPE12")
		# POST.objects.create(author=author, course=course, num_upvotes=4, num_downvotes=1, 
		# 	num_views=100, isNotes=False)


		post_id = request.data['post_id']
		post = POST.objects.filter(post_id=post_id)
		on = request.data['on']
		if len(post) :
			print(post.isNotes)
			if on == "1":
				post.num_upvotes+=1
				if post.isNotes is True:
					post.author.total_upvotes_notes+=1
				else :
					post.author.total_upvotes_assignments+=1

			else:
				post.num_upvotes-=1
				if post.isNotes is True:
					post.author.total_upvotes_notes-=1
				else :
					post.author.total_upvotes_assignments-=1
			post.save()
			post.author.save()
			print(post.num_upvotes)
			print(post.author.total_upvotes_notes)
			print(post.author.total_upvotes_assignments)
			js = json.dumps({"status" : "true", "msg" : "Upvote Done"})
			return Response(js, status=status.HTTP_200_OK)
		else:
			js = json.dumps({"status" : "false", "msg" : "Invalid Upvote Request"})
			return Response(js, status=status.HTTP_400_BAD_REQUEST)