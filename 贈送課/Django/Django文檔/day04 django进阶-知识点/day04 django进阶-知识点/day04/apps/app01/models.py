from django.db import models


class Department(models.Model):
    """部门表"""
    title = models.CharField(verbose_name="标题")


class UserInfo(models.Model):
    """用户表"""
    name = models.CharField(verbose_name="姓名")

    depart = models.ForeignKey(verbose_name="部门ID", to="Department", to_field="id", on_delete=models.CASCADE, db_constraint=False)
    # depart = models.ForeignKey(verbose_name="部门ID", to="Department", to_field="id", on_delete=models.SET_NULL,null=True,blank=True)
    # depart = models.ForeignKey(verbose_name="部门ID", to="Department", to_field="id", on_delete=models.SET_DEFAULT, default=2)


class Boy(models.Model):
    name = models.CharField(verbose_name="姓名")


class Girl(models.Model):
    name = models.CharField(verbose_name="姓名")
    relation = models.ManyToManyField(verbose_name="男女关系", to="Boy")











