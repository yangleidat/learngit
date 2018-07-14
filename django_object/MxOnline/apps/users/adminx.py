# _*_ coding:utf-8 _*_
__author__ = 'YL007'
__date__ = '2018/7/14 12:50'

import xadmin
from xadmin import views

from .models import EmailVerifyRecord,Banner


class BaseSetting(object):
    '''主题'''
    enable_themes = True #开启主题功能
    use_bootswatch = True


class GlobalSetting(object):
    '''全局设置'''
    site_title = '幕学后台管理系统' #左上角标题
    site_footer = '幕学在线网' #页脚
    menu_style = 'accordion' #收起页面左侧app列表


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']

class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)