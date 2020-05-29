from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializers(serializers.ModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
        
    class Meta:
        model = get_user_model()
        fields = ( 'id','username','email','password','is_superuser')