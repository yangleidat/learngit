from django.db import models
from datetime import datetime

# Create your models here.

class DataTable(models.Model):
    name = models.CharField(max_length=16, verbose_name=u'对接人姓名')
    mobile = models.CharField(max_length=11, verbose_name=u'对接人电话')
    service = models.CharField(max_length=10, verbose_name=u'服务内容')
    waiting_time = models.CharField(max_length=6, verbose_name=u'等待对接时长')
    overall_satisfaction = models.CharField(max_length=6, verbose_name=u'现场及调度满意度')
    attitude = models.CharField(max_length=6, verbose_name=u'人员态度满意度')
    cycle = models.CharField(max_length=6, verbose_name=u'作业周期')
    eat = models.CharField(max_length=2, verbose_name=u'是否用餐或发放餐券')
    proposal = models.CharField(max_length=500, verbose_name=u'建议')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'数据表'
        verbose_name_plural = verbose_name