# Create your views here.
from django.http import HttpRequest, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .custom_serializers import PeopleSerializer, SubjectAllSerializer, SubjectVoSerializer, TeacherSerializer
from .models import Subject, People, Teacher


@api_view(('GET',))
def show_subjects(request: HttpRequest) -> HttpResponse:
    subjects = Subject.objects.all().order_by('no')
    # 创建序列化器对象并指定要序列化的模型
    serializer = SubjectAllSerializer(subjects, many=True)
    # 通过序列化器的data属性获得模型对应的字典并通过创建Response对象返回JSON格式的数据
    return Response(serializer.data)


@api_view(('GET',))
def show_teachers(request: HttpRequest) -> HttpResponse:
    try:
        sno = int(request.GET.get('sno'))
        subject = Subject.objects.only('name').get(no=sno)
        teachers = Teacher.objects.filter(subject=subject).defer('subject').order_by('no')
        subject_seri = SubjectVoSerializer(subject)
        teacher_seri = TeacherSerializer(teachers, many=True)
        return Response({'subject': subject_seri.data, 'teachers': teacher_seri.data})
    except (TypeError, ValueError, Subject.DoesNotExist):
        return Response(status=404)


@api_view(('GET',))
def get_people(request: HttpRequest) -> HttpResponse:
    subject = People('zjy', 18)
    # 创建序列化器对象并指定要序列化的模型
    serializer = PeopleSerializer(subject)
    # 通过序列化器的data属性获得模型对应的字典并通过创建Response对象返回JSON格式的数据
    return Response(serializer.data)
