from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
import json
from rest_framework.permissions import AllowAny

# Create your views here.
class AddCourse(APIView): #Logins the user based on username,password and isStudent field sent from Client Side and returns the corresponding token
	""" 
	Logs in the user. 
	"""
	permission_classes = (AllowAny,)
	def post(self,request,format='json'):

		

		user = request.user
		
		
		if user is not None:
			if user.is_active:
				if request.data["type"] == "1":
					if user.username == "admin":
						branch_name = request["branch"]
						course_id = request["course_id"]
						course_name = request["course_name"]
						branch = BRANCH.objects.get(branch_name=branch_name)
						course = COURSE.objects.filter(course_id=course_id)
						if len(course) == 0:
							course = COURSE.objects.create(course_id=course_id, 
								course_name=course_name)
							course.save()
						else:
							js = json.dumps({"status" : "false", "msg" : "Course already exists"})
							return Response(js, status=status.HTTP_400_BAD_REQUEST)

						js = json.dumps({"status" : "true", "msg" : "Course added successfully"})
						return Response(js, status=status.HTTP_200_OK)
					else:
						js = json.dumps({"status" : "false", "msg" : "Not a valid admin"})
						return Response(js, status=status.HTTP_400_BAD_REQUEST)
				else:
					#Second Portion Code
					print("HEYYY")

				
			else:
				js = json.dumps({"status" : "false", "reason" : "You need to activate your account. Please check your email"})
				return Response(js, status=status.HTTP_400_BAD_REQUEST)
		else:
				js = json.dumps({"status" : "false", "reason" : "Invalid username/password"})
				return Response(js, status=status.HTTP_400_BAD_REQUEST)
