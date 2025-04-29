from django.db import models


class Boy(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=32, db_index=True)


class Girl(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=32, db_index=True)


class B2G(models.Model):
    bid = models.ForeignKey(to="Boy", on_delete=models.CASCADE)
    gid = models.ForeignKey(to="Girl", on_delete=models.CASCADE)
    address = models.CharField(verbose_name="地点", max_length=32)


class Depart(models.Model):
    """ 部门 """
    title = models.CharField(verbose_name="标题", max_length=32)


class Admin(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=32)
    pwd = models.CharField(verbose_name="密码", max_length=32)

    depart = models.ForeignKey(verbose_name="部门", to="Depart", on_delete=models.CASCADE, related_name='d1')
    new_depart = models.ForeignKey(verbose_name="新部门", to="Depart", on_delete=models.CASCADE, related_name='d2',
                                   default=2)


class Role(models.Model):
    title = models.CharField(verbose_name="姓名", max_length=32)
    od = models.IntegerField(verbose_name="排序", default=0)

    def __str__(self):
        return "{}-{}".format(self.id, self.title)


class UserInfo(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=32, db_index=True)
    pwd = models.CharField(verbose_name="密码", max_length=32)


class Blog(models.Model):
    user = models.OneToOneField(to="UserInfo", on_delete=models.CASCADE)
    blog = models.CharField(verbose_name="博客地址", max_length=255)
    summary = models.CharField(verbose_name="简介", max_length=128)
