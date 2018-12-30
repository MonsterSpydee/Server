from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from Server.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Accounts.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate, login
import json

class UserCreate(APIView): #Creates a user object based on the data sent from Client side and returns the token corresponding to the user
	"""
	Creates the user.
	"""
	permission_classes = (AllowAny,)
	def post(self, request, format='json'):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			#print("Valid")
			user = serializer.save()
			token = Token.objects.create(user=user)
			json = serializer.data
			json['token'] = token.key
			return Response(json, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView): #Logins the user based on username,password and isStudent field sent from Client Side and returns the corresponding token
	""" 
	Logs in the user. 
	"""
	permission_classes = (AllowAny,)
	def post(self,request,format='json'):

		username = request.data['username']
		password = request.data['password']

		user = authenticate(username=username, password=password)
		
		
		if user is not None:
			if user.is_active:
				if request.data["isAdmin"] == "1":
					if username == "admin" and password == "admin" :
						login(request, user)
						token, created = Token.objects.get_or_create(user=user)
						js = json.dumps({"status" : "true", "token" : token.key})
						return Response(js, status=status.HTTP_200_OK)
					else:
						js = json.dumps({"status" : "false", "msg" : "Not a valid admin"})
						return Response(js, status=status.HTTP_400_BAD_REQUEST)
				else:
					login(request, user)
					token, created = Token.objects.get_or_create(user=user)
					js = json.dumps({"status" : "true", "token" : token.key})
					return Response(js, status=status.HTTP_200_OK)

				
			else:
				js = json.dumps({"status" : "false", "reason" : "You need to activate your account. Please check your email"})
				return Response(js, status=status.HTTP_400_BAD_REQUEST)
		else:
				js = json.dumps({"status" : "false", "reason" : "Invalid username/password"})
				return Response(js, status=status.HTTP_400_BAD_REQUEST)
