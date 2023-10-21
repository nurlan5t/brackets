from rest_framework import serializers
from bracketsapp.models import Journal


class JournalsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'

    def create(self, validated_data):
        return Journal.objects.create(**validated_data)

# class JournalsCreateSerializer(serializers.Serializer):
#     input_data = serializers.CharField(required=True)

    # def create(self, validated_data):
    #     return Journal.objects.create(**validated_data)
