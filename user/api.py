# from django.shortcuts import render
from lib.http import render_json
from common import error
from user.logic import send_verify_code, check_vcode
from user.models import User

# Create your views here.

def get_verify_code(request):
    """手机注册"""
    phonenum = request.POST.get('phonenum')
    send_verify_code(phonenum)
    return render_json(None, 0)

def login(request):
    """短信验证登陆"""
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    if check_vcode(phonenum, vcode): #正常处理
    # if vcode == '123456':#测试用
        # 验证成功,获取用户,第一次登陆,直接手机号注册
        user, created = User.objects.get_or_create(phonenum=phonenum)
        # 记录登陆状态，保存session的值到服务器
        request.session['uid'] = user.id
        return render_json(user.to_dict(), 0)
    else:
        return render_json(None, error.VCODE_ERROR)


def get_profile(request):
    """获取个人资料"""
    pass


def modify_profile(request):
    """修改个人资料"""
    pass


def upload_avatar(request):
    """头像上传"""
    pass
