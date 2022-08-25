import datetime

from user.models import User
from social.models import Swiped, Friend


def get_rcmd_users(user):
    """
    获取推荐用户
    """
    sex = user.profile.dating_sex
    location = user.profile.location
    min_age = user.profile.min_dating_age
    max_age = user.profile.max_dating_age

    current_year = datetime.date.today().year
    min_age_year = current_year - min_age
    max_age_year = current_year - max_age

    # 这里是懒加载，其实就是延时加载，即当对象需要用到的时候再去加载,
    # 当系统或者开发者调用对象的取对象的方法时，再去加载对象
    users = User.objects.filter(sex=sex, location=location,
                                birth_year__gte=max_age_year,
                                birth_year__lte=min_age_year)
    return users


def like(user, sid):
    """喜欢一个用户"""
    Swiped.mark(user.id, sid, 'like')
    # 检查被滑动的用户是否喜欢过自己
    if Swiped.is_liked(sid, user.id):
        # 两个人都相互喜欢则标记为好友,即创建好友关系
        Friend.be_friends(user.id, sid)
        return True
    else:
        return False


def superlike(user, sid):
    Swiped.mark(user.id, sid, 'superlike')
    if Swiped.is_liked(sid, user.id):
        Friend.be_friends(user.id, sid)
        return True
    else:
        return False


def dislike(user, sid):
    Swiped.mark(user.id, sid, 'dislike')


def rewind(user, sid):
    """反悔"""
    try:
        # 删除滑动记录
        Swiped.objects.get(uid=user.id, sid=sid).delete()
    except Swiped.DoesNotExist:
        pass
    # 删除好友关系
    Friend.break_off(user.id, sid)

