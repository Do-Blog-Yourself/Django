from rest_framework import serializers
from API.models import MyUser

class MyUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    account_updated = serializers.DateTimeField()
    account_created = serializers.DateTimeField()
    password = serializers.CharField(read_only=True)
    username= serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return MyUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance