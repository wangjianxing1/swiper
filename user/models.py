import datetime

from django.db import models
from django.utils.functional import cached_property


# Create your models here.

class User(models.Model):
    """用户数据模型"""
    SEX = (
        ('M', '男'),
        ('F', '女'),
    )
    nickname = models.CharField(max_length=32, unique=True)
    phonenum = models.CharField(max_length=16, unique=True)
    sex = models.CharField(max_length=8, choices=SEX)
    birth_year = models.IntegerField(default=2000)
    birth_month = models.IntegerField(default=1)
    birth_day = models.IntegerField(default=1)
    avatar = models.ImageField(max_length=256)
    location = models.CharField(max_length=32)

    """年龄只计算一次，
    变成属性加在变量身上，
    和下面的配置项方法原理一样"""

    @cached_property
    def age(self):
        today = datetime.date.today()
        birth_date = datetime.date(self.birth_year, self.birth_month, self.birth_day)
        return (today - birth_date).days // 365

    @property
    def profile(self):
        """用户的配置项，构建两张表的关联"""
        if not hasattr(self, '_profile'):
            self._profile, _ = Profile.objects.get_or_create(id=self.id)
        return self._profile


class Profile(models.Model):
    """"用户配置项"""
    SEX = (
        ('M', '男'),
        ('F', '女'),
    )
    location = models.CharField(max_length=32, verbose_name='目标城市')

    min_distance = models.IntegerField(default=1, verbose_name='最小查找范围')
    max_distance = models.IntegerField(default=10, verbose_name='最大查找范围')

    min_dating_age = models.IntegerField(default=18, verbose_name='最小交友年龄')
    max_dating_age = models.IntegerField(default=45, verbose_name='最大交友年龄')

    dating_sex = models.CharField(default='女', max_length=8, choices=SEX, verbose_name='匹配性别')
    vibration = models.BooleanField(default=True, verbose_name='开启振动')
    only_matche = models.BooleanField(default=True, verbose_name='不让为匹配的人看我的相册')
    auto_play = models.BooleanField(default=True, verbose_name='自动播放视频')
