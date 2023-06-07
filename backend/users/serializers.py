from .models import User

from rest_framework import serializers


class UserCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating a new user"""

    # password = serializers.CharField(write_only=True)

    # email = serializers.EmailField()
    
    # first_name = serializers.CharField(max_length=30)

    # last_name = serializers.CharField(max_length=30)
    # username = serializers.CharField(max_length=30)

    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'profile_pic',
            'address',
            'city' ,
            'state',
            'zip_code',
            'phone',
        ]

    def create(self, validated_data):
        """Create a new user"""
        password = self.context['request'].data.get('password')
        user=User(**validated_data)
        user.generate_hashed_password(password)
        user.save()
        return user
        


# class UserToken(serializers.Serializer)