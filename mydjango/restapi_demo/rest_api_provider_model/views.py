# Create your views here.
import logging

from django.http import HttpRequest, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .custom_serializers import PeopleSerializer, SubjectAllSerializer, SubjectVoSerializer, TeacherSerializer
from .models import Subject, People, Teacher


# FBV（基于函数的视图）
@api_view(('GET',))
def show_subjects(request: HttpRequest) -> HttpResponse:
    subjects = Subject.objects.all().order_by('no')
    # 创建序列化器对象并指定要序列化的模型
    serializer = SubjectAllSerializer(subjects, many=True)
    # 通过序列化器的data属性获得模型对应的字典并通过创建Response对象返回JSON格式的数据
    return Response(serializer.data)


# FBV（基于函数的视图）
@api_view(('GET',))
def show_teachers(request: HttpRequest) -> HttpResponse:
    try:
        sno = int(request.GET.get('sno'))
        subject = Subject.objects.only('name').get(no=sno)
        teachers = Teacher.objects.filter(subject=subject).defer('subject').order_by('no')
        subject_serializer = SubjectVoSerializer(subject)
        teacher_serializer = TeacherSerializer(teachers, many=True)
        return Response({'subject': subject_serializer.data, 'teachers': teacher_serializer.data})
    except (TypeError, ValueError, Subject.DoesNotExist) as e:
        logging.error(e)
        return Response(status=404)


# FBV（基于函数的视图）
@api_view(('GET',))
def get_people(request: HttpRequest) -> HttpResponse:
    subject = People('zjy', 18)
    # 创建序列化器对象并指定要序列化的模型
    serializer = PeopleSerializer(subject)
    # 通过序列化器的data属性获得模型对应的字典并通过创建Response对象返回JSON格式的数据
    return Response(serializer.data)


# CBV（基于类的视图）
class SubjectView(ListAPIView):
    """
    它封装了获取数据列表并返回JSON数据的get方法。
    ListAPIView是APIView 的子类，APIView还有很多的子类,例如:
    CreateAPIView可以支持POST请求
    UpdateAPIView可以支持PUT和PATCH请求
    DestoryAPIView可以支持DELETE请求
    """
    # 通过queryset指定如何获取学科数据
    queryset = Subject.objects.all()
    # 通过serializer_class指定如何序列化学科数据
    serializer_class = SubjectAllSerializer


# 自定义分页
class CustomizedPagination(PageNumberPagination):
    # 默认页面大小
    page_size = 5
    # 页面大小对应的查询参数
    page_size_query_param = 'size'
    # 页面大小的最大值
    max_page_size = 50


class SubjectViewSet(ModelViewSet):
    """
    ModelViewSet共有6个父类
    其中前5个父类分别实现对
    POST（新增学科）、GET（获取指定学科）、PUT/PATCH（更新学科）、DELETE（删除学科）和GET（获取学科列表）操作的支持
    对应的方法分别是create、retrieve、update、destroy和list
        请求	    url	                                        对应方法
        get	    127.0.0.1:8000/rest-api/subjects/	        list
        get 	127.0.0.1:8000/rest-api/subjects/{1}/       retrieve
        post	127.0.0.1:8000/rest-api/book/               create
        put	    127.0.0.1:8000/rest-api/subjects/{1}/       update
        delete	127.0.0.1:8000/rest-api/subjects/{1}/       destroy
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectAllSerializer
    # 可以自定义分页
    # pagination_class = CustomizedPagination


class SubjectReadOnlyViewSet(ReadOnlyModelViewSet):
    """
    除了ModelViewSet类外，DRF还提供了一个名为ReadOnlyModelViewSet
    该类是只读视图的集合，继承该类定制的数据接口只能支持GET请求，也就是获取单个资源和资源列表的请求
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectAllSerializer
