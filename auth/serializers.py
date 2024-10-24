from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from library.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        groups = validated_data.pop('groups', None)
        user_permissions = validated_data.pop('user_permissions', None)

        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)

        instance.save()

        if groups:
            instance.groups.set(groups)
        if user_permissions:
            instance.user_permissions.set(user_permissions)

        return instance
