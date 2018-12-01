from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import POINTS
from .serializers import POINTSSerializer
import json
from rest_framework import status

class pointsList(APIView):
	def get(self,request):
		points = POINTS.objects.all()
		serializer = POINTSSerializer(points, many = True)
		return Response(serializer.data)

	def post(self,request,format ='json'):
		serializer = POINTSSerializer(data = request.data)
		if serializer.is_valid():
			new_point = POINTS(notes_upvote = request.data["notes_upvote"], 
				notes_downvote = request.data["notes_downvote"], assignments_upvote = request.data["assignments_upvote"], assignments_downvote = request.data["assignments_downvote"] )
			new_point.save()
			#print(new_point)
			js = json.dumps({"status" : "true", "msg" : "Points object created"})
			return Response(js, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.