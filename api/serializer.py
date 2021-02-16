from rest_framework import serializers
from .models import Data
from django.contrib.auth.models import User


class DataSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Data
        fields = ['fio', 'balance', 'status']


class DataSerializerAdd(serializers.HyperlinkedModelSerializer):

    def update(self, instance, validated_data):
        instance.balance += validated_data.get('balance', instance.balance)
        instance.save()
        return instance

    class Meta:
        model = Data
        fields = ['uuid', 'fio', 'balance', 'hold', 'status']


class DataSerializerSubstract(serializers.HyperlinkedModelSerializer):

    def update(self, instance, validated_data):
        if instance.balance - (validated_data.get('balance', instance.balance) + instance.hold) > 0:
            instance.balance -= (validated_data.get('balance',
                                                    instance.balance) + instance.hold)
            instance.save()
        else:
            raise serializers.ValidationError(
                ('Not enough money')
            )
        return instance

    class Meta:
        model = Data
        fields = ['uuid', 'fio', 'balance', 'hold', 'status']
