"""
vip - user: 一对多
vip - permission: 多对多
"""


from django.db import models

# Create your models here.

class Vip(models.Model):
    name = models.CharField(max_length=32, unique=True)
    level = models.IntegerField()
    price = models.FloatField()

    def perms(self):
        """获取当前VIP具有的所有权限"""
        relations = VipPermRelation.objects.filter(vip_id=self.id)
        # perms = []
        # for relation in relations:
        #     perm = Permission.objects.get(id = relation.perm_id)
        #     perms.append(perm)
        # return perms
        perm_id_list = [r.perm_id for r in relations]
        return Permission.objects.filter(id__in=perm_id_list)

    def has_perm(self, perm_name):
        """检查是否具有某种权限"""
        perm = Permission.objects.get(name=perm_name)
        return VipPermRelation.objects.filter(vip_id=self.id, perm_id=perm.id).exists()


class Permission(models.Model):
    """
    权限
        会员身份标识
        超级喜欢
        反悔功能
        任意更改定位
        无限喜欢次数
    """
    name = models.CharField(max_length=32, unique=True)


class VipPermRelation(models.Model):
    """会员权限关系表 多对多"""
    vip_id= models.IntegerField()
    perm_id = models.IntegerField()