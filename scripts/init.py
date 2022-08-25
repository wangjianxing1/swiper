#! /usr/bin/env python
# 创造虚拟假人

import os
import sys
import random

import django

# 设置环境
print('os.path.abspath(__file__):', os.path.abspath(__file__))
print('os.path.dirname(os.path.abspath(__file__):', os.path.dirname(os.path.abspath(__file__)))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print('BASE_DIR:', BASE_DIR)

sys.path.insert(0, BASE_DIR)

print('sys.path:', sys.path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swiper.settings")
django.setup()

from user.models import User

last_names = (
    '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨'
    '朱秦尤许何吕施张孔曹严华金魏陶姜'
    '戚谢邹喻柏水窦章云苏潘葛奚范彭郎'
    '鲁韦昌马苗凤花方俞任袁柳酆鲍史唐'
    '费廉岑薛雷贺倪汤滕殷罗毕郝邬安常'
    '乐于时傅皮卞齐康伍余元卜顾孟平黄'
)

first_names = {
    '男': [
        '弘文', '烨伟', '苑博', '鹏涛', '炎彬',
        '燃烧', '鹤轩', '伟泽', '君昊', '熠彤',
        '鸿煊', '博涛', '苑杰', '黎昕', '烨霖',
        '哲瀚', '雨泽', '楷瑞', '建辉', '致远',
        '鸿恩', '希文', '希诚', '希武', '玄华',
        '玄晋',
    ],
    '女': [
        '珊凤', '寄瑶', '水云', '琪珊', '欣华',
        '春妍', '碧丝', '含芷', '雅雪', '寒宁',
        '珊柳', '翠颖', '珊琴', '知秋', '怀落',
        '繁锦', '琴心', '晚照', '桑田', '语出',
        '玉珍', '茹雪', '正梅', '美琳', '欢馨',
        '优璇', '雨嘉', '娅楠', '明美', '可馨',
        '惠茜', '漫妮', '香茹', '月婵', '嫦曦',
        '梦洁', '静香', '美莲', '雅静', '凌薇'
    ]
}


def random_name():
    last_name = random.choice(last_names)
    sex = random.choice(list(first_names.keys()))
    first_name = random.choice(first_names[sex])
    return ''.join([last_name, first_name]), sex


for i in range(1000):
    name, sex = random_name()
    try:
        User.objects.create(
            phonenum='%s' % random.randrange(21000000000, 21900000000),
            nickname=name,
            sex=sex,
            birth_year=random.randint(1980, 2000),
            birth_month=random.randint(1, 12),
            birth_day=random.randint(1, 28),
            location=random.choice(['北京', '上海', '深圳', '成都', '西安', '武汉']),
            avatar='http://rgz4dtvve.hn-bkt.clouddn.com/Avatar-2'
        )
        print('created: %s %s' % (name, sex))
    except django.db.utils.IntegrityError:
        pass
