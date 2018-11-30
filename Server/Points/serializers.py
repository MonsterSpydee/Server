from rest_framework import serializers
from .models import POINTS

class POINTSSerializer(serializers.ModelSerializer):
	class Meta:
		model = POINTS
		fields = '__all__'