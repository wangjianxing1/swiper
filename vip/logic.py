from vip.models import Vip
from lib.http import render_json
from common import error


def perm_require(perm_name):
    """权限检查装饰器"""

    def deco(view_func):
        def wrap(request):
            user = request.user
            vip = Vip.objects.get(id=user.vip_id)
            if vip.has_perm(perm_name):
                response = view_func(request)
                return response
            else:
                return render_json(None, error.NOT_HAS_PERM)

        return wrap

    return deco


def perm_require1(perm_name):
    def perm_require(perm_name):
        """权限检查装饰器"""

        def deco(view_func):
            def wrap(request):
                user = request.user
                if user.vip.has_perm(perm_name):
                    response = view_func(request)
                    return response
                else:
                    return render_json(None, error.NOT_HAS_PERM)

            return wrap

        return deco
