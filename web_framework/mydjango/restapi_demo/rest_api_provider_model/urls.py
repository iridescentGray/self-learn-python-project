"""
URL configuration for web_config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (SubjectView, SubjectViewSet, get_people, show_subjects,
                    show_teachers)

# 通过router注册url
router = DefaultRouter()
# ModelViewSet相当于是多个视图函数的汇总，所以不同于之前映射URL的方式
# 需要我们先创建一个路由器并通过它注册SubjectViewSet，然后将注册成功后生成的URL一并添加到urlspattern列表中
router.register("subjects", SubjectViewSet)

# 手动注册url
urlpatterns = [
    path("show_subjects/", show_subjects),  # FBV（基于函数的视图）风格
    path("cbv_show_subjects/", SubjectView.as_view()),  # CBV（基于类的视图）风格
    path("", include(router.urls)),  # CBV（基于类的视图）风格
    path("show_teachers/", show_teachers),  # FBV（基于函数的视图）风格
    path("cbv_show_teachers/", show_teachers),  # CBV（基于类的视图）风格
    path("show_people/", get_people),
]
