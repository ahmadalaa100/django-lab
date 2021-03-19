from rest_framework import serializers
from netflix.models import movie
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["username",'email','password','password1']


    def save(self,**kwargs):
        user= User(
            email=self.validate_data.get('email'),
            username=self.validate_data.get('username')
        )

        if self.validate_data.get('password') !=  self.validate_data.get('password1'):
            raise serializers.validationError({
                "password": "passwords does not match !"
            })
        else:
            user.set_password(self.validate_data.get('password'))
            user.save()

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie
        fields = "__all__"