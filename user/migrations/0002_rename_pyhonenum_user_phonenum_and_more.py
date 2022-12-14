# Generated by Django 4.1 on 2022-08-13 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='pyhonenum',
            new_name='phonenum',
        ),
        migrations.AlterField(
            model_name='profile',
            name='dating_sex',
            field=models.CharField(choices=[('M', '男'), ('F', '女')], default='女', max_length=8, verbose_name='匹配性别'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_day',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_month',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_year',
            field=models.IntegerField(default=2000),
        ),
    ]
