from rest_framework import serializers
from .models import Klass, Mexmonxona, Travel

class KlassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klass
        fields = ['id', 'name', 'price']

    def create(self, validated_data):
        return Klass.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

class MexmonxonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mexmonxona
        fields = ['id', 'name', 'price', 'yulduzlar']

    def create(self, validated_data):
        return Mexmonxona.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.yulduzlar = validated_data.get('yulduzlar', instance.yulduzlar)
        instance.save()
        return instance

class TravelSerializer(serializers.ModelSerializer):
    klass = KlassSerializer()
    mexmonxona = MexmonxonaSerializer()

    class Meta:
        model = Travel
        fields = ['id', 'name', 'destination', 'created', 'modified', 'klass', 'mexmonxona']

    def create(self, validated_data):
        klass_data = validated_data.pop('klass', None)
        mexmonxona_data = validated_data.pop('mexmonxona', None)

        travel = Travel.objects.create(**validated_data)

        if klass_data:
            klass = Klass.objects.create(**klass_data)
            travel.klass = klass

        if mexmonxona_data:
            mexmonxona = Mexmonxona.objects.create(**mexmonxona_data)
            travel.mexmonxona = mexmonxona

        travel.save()
        return travel

    def update(self, instance, validated_data):
        klass_data = validated_data.pop('klass', None)
        mexmonxona_data = validated_data.pop('mexmonxona', None)

        instance.name = validated_data.get('name', instance.name)
        instance.destination = validated_data.get('destination', instance.destination)
        instance.save()

        if klass_data:
            klass_serializer = KlassSerializer(instance.klass, data=klass_data)
            if klass_serializer.is_valid():
                klass_serializer.save()

        if mexmonxona_data:
            mexmonxona_serializer = MexmonxonaSerializer(instance.mexmonxona, data=mexmonxona_data)
            if mexmonxona_serializer.is_valid():
                mexmonxona_serializer.save()

        return instance
