# Generated by Django 4.1 on 2022-08-13 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=32, verbose_name='目标城市')),
                ('min_distance', models.IntegerField(default=1, verbose_name='最小查找范围')),
                ('max_distance', models.IntegerField(default=10, verbose_name='最大查找范围')),
                ('min_dating_age', models.IntegerField(default=18, verbose_name='最小交友年龄')),
                ('max_dating_age', models.IntegerField(default=45, verbose_name='最大交友年龄')),
                ('dating_sex', models.CharField(choices=[('M', '男'), ('F', '女')], max_length=8, verbose_name='匹配性别')),
                ('vibration', models.BooleanField(default=True, verbose_name='开启振动')),
                ('only_matche', models.BooleanField(default=True, verbose_name='不让为匹配的人看我的相册')),
                ('auto_play', models.BooleanField(default=True, verbose_name='自动播放视频')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=32, unique=True)),
                ('pyhonenum', models.CharField(max_length=16, unique=True)),
                ('sex', models.CharField(choices=[('M', '男'), ('F', '女')], max_length=8)),
                ('birth_year', models.IntegerField()),
                ('birth_month', models.IntegerField()),
                ('birth_day', models.IntegerField()),
                ('avatar', models.ImageField(max_length=256, upload_to='')),
                ('location', models.CharField(max_length=32)),
            ],
        ),
    ]
