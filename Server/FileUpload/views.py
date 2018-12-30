from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
import json
from Course_Branch.models import COURSE
from Post.models import POST

class FileView(APIView):
	parser_classes = (MultiPartParser, FormParser)
	
	def post(self, request, *args, **kwargs):
		user = request.user
		if user is not None:
			if user.is_active:
				file_serializer = FileSerializer(data=request.data)
				if file_serializer.is_valid():
					content = file_serializer.save()
					course = COURSE.objects.filter(course_id=request.data['course_id'])
					post = POST.objects.create(isNotes=request.data['isNotes'], course=course, author=user)
					post.content = content
					post.save()
					return Response(file_serializer.data, status=status.HTTP_201_CREATED)
				else:
					return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		js = json.dumps({"status" : "false", "msg" : "Not logged in"})
		return Response(js, status=status.HTTP_400_BAD_REQUEST)