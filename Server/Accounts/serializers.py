from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from Server.models import User

class UserSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(min_length=1, max_length=100,
            write_only=True)
    last_name = serializers.CharField(min_length=1, max_length=100,
            write_only=True)
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            max_length=32,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=6, max_length=100,
            write_only=True)

    branch = serializers.CharField(min_length=3, max_length=10,
            write_only=True)

    

    def create(self, validated_data):
        user = User(email=validated_data['email'],
                username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password', 'branch')
