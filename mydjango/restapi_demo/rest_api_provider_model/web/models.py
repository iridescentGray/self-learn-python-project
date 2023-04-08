# Create your models here.
from django.db import models


# 模型字段请参考 https://docs.djangoproject.com/zh-hans/4.0/ref/models/fields/
class Subject(models.Model):
    no = models.AutoField(primary_key=True, verbose_name='编号')
    name = models.CharField(max_length=50, verbose_name='名称')
    intro = models.CharField(max_length=1000, verbose_name='介绍')
    is_hot = models.BooleanField(verbose_name='是否热门')

    class Meta:
        managed = False
        db_table = 'tb_subject'


class Teacher(models.Model):
    no = models.AutoField(primary_key=True, verbose_name='编号')
    name = models.CharField(max_length=20, verbose_name='姓名')
    sex = models.BooleanField(default=True, verbose_name='性别')
    birth = models.DateField(verbose_name='出生日期')
    intro = models.CharField(max_length=1000, verbose_name='个人介绍')
    photo = models.ImageField(max_length=255, verbose_name='照片')
    good_count = models.IntegerField(default=0, db_column='gcount', verbose_name='好评数')
    bad_count = models.IntegerField(default=0, db_column='bcount', verbose_name='差评数')
    subject = models.ForeignKey(Subject, models.DO_NOTHING, db_column='sno')

    class Meta:
        managed = False
        db_table = 'tb_teacher'


class People:

    def __init__(self, name, age, is_student=False, score=100):
        self.name = name
        self.age = age
        self._is_student = is_student
        self.score = score

    @property
    def source(self):
        return self.score
