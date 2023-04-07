# Create your models here.

from rest_framework import serializers

from django.restapi_demo.rest_api_provider_model.src.domain.subject import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
