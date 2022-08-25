import datetime

from user.models import User

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