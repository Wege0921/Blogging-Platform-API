# users/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile
from django.contrib.auth.password_validation import validate_password

CustomUser = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    profile_pic = serializers.ImageField(source='profile.profile_pic', required=False)
    bio = serializers.CharField(source='profile.bio', required=False)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'date_of_birth', 'password', 'profile_pic', 'bio']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', {})
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            date_of_birth=validated_data.get('date_of_birth')
        )
        Profile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)

        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        
        instance.save()

        # Update or create user profile
        profile = instance.profile
        profile.bio = profile_data.get('bio', profile.bio)
        profile.profile_pic = profile_data.get('profile_pic', profile.profile_pic)
        profile.save()

        return instance


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic']
