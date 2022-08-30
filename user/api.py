# from django.shortcuts import render

from django.core.cache import cache

from lib.http import render_json
from common import error
from user.logic import send_verify_code, check_vcode, save_upload_file
from user.models import User
from user.forms import ProfileForm

from swiper import settings

# Create your views here.

def get_verify_code(request):
    """手机注册"""
    phonenum = request.POST.get('phonenum')
    send_verify_code(phonenum)
    return render_json(None)

def login(request):
    """短信验证登陆"""
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    # if check_vcode(phonenum, vcode): #正常处理
    if vcode == '123456':#测试用
        # 验证成功,获取用户,第一次登陆,直接手机号注册
        user, created = User.objects.get_or_create(phonenum=phonenum)
        # 记录登陆状态，保存session的值到服务器
        request.session['uid'] = user.id
        return render_json(user.to_dict())
    else:
        return render_json(None, error.VCODE_ERROR)


def get_profile(request):
    """获取个人资料"""
    user = request.user
    key = 'Profile-%s' % user.id
    user_profile = cache.get(key)
    print('get from redis-cache: %s' % user_profile)
    if not user_profile:
        user_profile = user.profile.to_dict()
        print('get from database: %s' % user_profile)
        cache.set(key, user_profile)
        print('add to redis-cache')
    return render_json(user_profile)


def modify_profile(request):
    """修改个人资料"""
    # request.POST是一个字典
    # if settings.DEBUG == True:
    #     import json
    #     data = json.loads(request.body)
    # else:
    #     data = request.POST
    data = request.POST
    form = ProfileForm(data)
    if form.is_valid():
        user = request.user
        user.profile.__dict__.update(form.cleaned_data)
        user.profile.save()
        # 修改缓存
        key = 'Profile-%s' % user.id
        cache.set(key, user.profile.to_dict())
        return render_json(None)
    else:
        return render_json(form.errors, error.PROFILE_ERROR)


def upload_avatar(request):
    """头像上传"""
    try:
        picture = request.FILES.get('avatar')
        save_upload_file(request.user, picture)
        return render_json(None)
    except:
        return render_json(None, error.PICTURE_NOT_FOUND)

    # picture = request.FILES.get('avatar')
    # if picture:
    #     # save_upload_file(request.session['uid'],picture )
    #     save_upload_file(request.user.id,picture )
    #     return render_json(None)
    # else:
    #     return render_json(None, error.PICTURE_NOT_FOUND)







