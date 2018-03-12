from rest_framework import serializers

from . import models as m


class RestAuthUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = m.User
        fields = ('email', 'password')
        read_only_fields = ('email',)
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = m.User
        fields = ('email', 'password')
        read_only_fields = ('email',)
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }