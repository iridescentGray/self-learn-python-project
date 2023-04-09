from rest_framework import serializers

from .models import Subject, Teacher


class SubjectAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class SubjectVoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('no', 'name')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        exclude = ('subject',)


class PeopleSerializer(serializers.Serializer):
    """
        People类的Serializer
    """
    age = serializers.CharField(max_length=200, )
    name = serializers.CharField(max_length=200, )
    _is_student = serializers.BooleanField()
    score = serializers.IntegerField()

    def update(self, instance, validated_data):
        """
        不实现
        :param instance:
        :param validated_data:
        :return:
        """
        pass

    def create(self, validated_data):
        """
        不实现
        :param validated_data:
        :return:
        """
        pass
