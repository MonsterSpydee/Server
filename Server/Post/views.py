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
		#User.objects.create(username="barry_19281", password="barry_19281", 
		 	#first_name="rajat")
		author = User.objects.get(username="barry_19281",password="barry_19281")

		# User.objects.create(username="pratikshya361", password="pratikshya361",
		# 	first_name="pratikshya")
		

		#BRANCH.objects.create(branch_id="CSE", branch_name="Computer Science and Engineering")
		branch = BRANCH.objects.get(branch_id="CSE")
		#COURSE.objects.create(course_id="CSPE12", course_name="DAPA", branch=branch)
		course = COURSE.objects.get(course_id="CSPE12")
		POST.objects.create(author=author, course=course, num_upvotes=4, num_downvotes=1, 
			num_views=100, isNotes=False)


		post_id = request.data['post_id']
		post = POST.objects.filter(post_id=post_id)
		on = request.data['on']
		if len(post) :
			print(post[0].isNotes)
			if on == "1":
				post[0].num_upvotes+=1
				if post[0].isNotes is True:
					post[0].author.total_upvotes_notes+=1
				else :
					post[0].author.total_upvotes_assignments+=1

			else:
				post[0].num_upvotes-=1
				if post[0].isNotes is True:
					post[0].author.total_upvotes_notes-=1
				else :
					post[0].author.total_upvotes_assignments-=1
			post[0].save()
			post[0].author.save()
			print(post[0].num_upvotes)
			print(post[0].author.total_upvotes_notes)
			print(post[0].author.total_upvotes_assignments)
			js = json.dumps({"status" : "true", "msg" : "Upvote Done"})
			return Response(js, status=status.HTTP_200_OK)
		else:
			js = json.dumps({"status" : "false", "msg" : "Invalid Upvote Request"})
			return Response(js, status=status.HTTP_400_BAD_REQUEST)

class downvoteView(APIView):
	def get(self, request):
		pass

	def post(self,request,format = 'json'):
		#User.objects.create(username="barry_19281", password="barry_19281", 
		 	#first_name="rajat")
		author = User.objects.get(username="barry_19281",password="barry_19281")

		# User.objects.create(username="pratikshya361", password="pratikshya361",
		# 	first_name="pratikshya")
		

		#BRANCH.objects.create(branch_id="CSE", branch_name="Computer Science and Engineering")
		branch = BRANCH.objects.get(branch_id="CSE")
		#COURSE.objects.create(course_id="CSPE12", course_name="DAPA", branch=branch)
		course = COURSE.objects.get(course_id="CSPE12")
		POST.objects.create(author=author, course=course, num_upvotes=1, num_downvotes=4, 
			num_views=100, isNotes=False)


		post_id = request.data['post_id']
		post = POST.objects.filter(post_id=post_id)
		on = request.data['on']
		if len(post) :
			print(post[0].isNotes)
			if on == "1":
				post[0].num_downvotes+=1
				if post[0].isNotes is True:
					post[0].author.total_downvotes_notes+=1
				else :
					post[0].author.total_downvotes_assignments+=1

			else:
				post[0].num_downvotes-=1
				if post[0].isNotes is True:
					post[0].author.total_downvotes_notes-=1
				else :
					post[0].author.total_downvotes_assignments-=1
			post[0].save()
			post[0].author.save()
			print(post[0].num_downvotes)
			print(post[0].author.total_downvotes_notes)
			print(post[0].author.total_downvotes_assignments)
			js = json.dumps({"status" : "true", "msg" : "Downvote Done"})
			return Response(js, status=status.HTTP_200_OK)
		else:
			js = json.dumps({"status" : "false", "msg" : "Invalid Downvote Request"})
			return Response(js, status=status.HTTP_400_BAD_REQUEST)

class numberOfViews(APIView):
	def get(self, request):
		pass

	def post(self,request,format = 'json'):
		#User.objects.create(username="barry_19281", password="barry_19281", 
		 	#first_name="rajat")
		author = User.objects.get(username="barry_19281",password="barry_19281")

		# User.objects.create(username="pratikshya361", password="pratikshya361",
		# 	first_name="pratikshya")
		

		#BRANCH.objects.create(branch_id="CSE", branch_name="Computer Science and Engineering")
		branch = BRANCH.objects.get(branch_id="CSE")
		#COURSE.objects.create(course_id="CSPE12", course_name="DAPA", branch=branch)
		course = COURSE.objects.get(course_id="CSPE12")
		POST.objects.create(author=author, course=course, num_upvotes=1, num_downvotes=4, 
			num_views=100, isNotes=False)


		post_id = request.data['post_id']
		post = POST.objects.filter(post_id=post_id)
		on = request.data['on']
		if len(post) :
			print(post[0].isNotes)
			post[0].num_views+=1			
			post[0].save()
			print(post[0].num_views)
			js = json.dumps({"status" : "true", "msg" : "Views updated"})
			return Response(js, status=status.HTTP_200_OK)
		else:
			js = json.dumps({"status" : "false", "msg" : "Invalid Views Request"})
			return Response(js, status=status.HTTP_400_BAD_REQUEST)