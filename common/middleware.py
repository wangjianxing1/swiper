from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from user.models import User
from lib.http import render_json
from common import error

class AuthMiddleware(MiddlewareMixin):
    """验证用户是否登陆中间件"""
    WHITE_LIST = [
        'user/verify_code',
        'user/login',
    ]

    def process_request(self, request):
        # 如果请求的URL在白名单内，直接跳过检查
        for path in self.WHITE_LIST:
            if request.path.startswith(path):
                return
        # 进行登陆检查
        uid = request.session.get('uid')
        if uid:
            try:
                request.user = User.objects.get(id=uid)
                return
            except User.DoesNotExist:
                request.session.flush() # 清除session设置无效的uid
        return render_json(None, error.LOGIN_ERROR)



# 可以用这个模块处理跨域,用了以后报错，所以此模块没有用

class CorsMiddleware(MiddlewareMixin):
    """通过响应客户端请求处理客户端的跨域"""
    def process_request(self, request):
        if request.method == 'OPTIONS' and 'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META:
            response = HttpResponse()
            response['Content-length'] = '0'
            response['Access-Control-Allow-Headers'] = request.META['HTTP_ACCESS_CONTROL_REQUEST_HEADERS']
            response['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8000'
            return response

    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8000'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response