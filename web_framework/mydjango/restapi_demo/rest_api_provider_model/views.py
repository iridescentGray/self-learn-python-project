# Create your views here.
import logging

from django.http import HttpRequest, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .custom_serializers import (PeopleSerializer, SubjectAllSerializer,
                                 SubjectVoSerializer, TeacherSerializer)
from .models import People, Subject, Teacher


# FBV（基于函数的视图）
@api_view(("GET",))
# 声明式缓存
@cache_page(timeout=86400, cache="default")
def show_subjects(request: HttpRequest) -> HttpResponse:
    subjects = Subject.objects.all().order_by("no")
    # 创建序列化器对象并指定要序列化的模型
    serializer = SubjectAllSerializer(subjects, many=True)
    # 通过序列化器的data属性获得模型对应的字典并通过创建Response对象返回JSON格式的数据
    return Response(serializer.data)


# 编程式缓存
# def show_subjects(request):
#     """获取学科数据"""
#     redis_cli = get_redis_connection()
#     # 先尝试从缓存中获取学科数据
#     data = redis_cli.get('rest_api_provider_model:restapi:subjects')
#     if data:
#         # 如果获取到学科数据就进行反序列化操作
#         data = json.loads(data)
#     else:
#         # 如果缓存中没有获取到学科数据就查询数据库
#         queryset = Subject.objects.all()
#         data = SubjectAllSerializer(queryset, many=True).data
#         # 将查到的学科数据序列化后放到缓存中
#         redis_cli.set('rest_api_provider_model:restapi:subjects', json.dumps(data), ex=86400)
#     return Response({'code': 200, 'subjects': data})


# FBV（基于函数的视图）
@api_view(("GET",))
def show_teachers(request: HttpRequest) -> HttpResponse:
    try:
        sno = int(request.GET.get("sno"))
        subject = Subject.objects.only("name").get(no=sno)
        teachers = (
            Teacher.objects.filter(subject=subject).defer("subject").order_by("no")
        )
        subject_serializer = SubjectVoSerializer(subject)
        teacher_serializer = TeacherSerializer(teachers, many=True)
        return Response(
            {"subject": subject_serializer.data, "teachers": teacher_serializer.data}
        )
    except (TypeError, ValueError, Subject.DoesNotExist) as e:
        logging.error(e)
        return Response(status=404)


# FBV（基于函数的视图）
@api_view(("GET",))
def get_people(request: HttpRequest) -> HttpResponse:
    subject = People("zjy", 18)
    # 创建序列化器对象并指定要序列化的模型
    serializer = PeopleSerializer(subject)
    # 通过序列化器的data属性获得模型对应的字典并通过创建Response对象返回JSON格式的数据
    return Response(serializer.data)


# CBV（基于类的视图）
# CBV，可以利用Django中名为method_decorator的装饰器将cache_page（cache_page装饰器不能直接放在类上）这个装饰到类中的方法上
@method_decorator(decorator=cache_page(timeout=86400, cache="default"), name="get")
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
    page_size_query_param = "size"
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
