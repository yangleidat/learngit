# _*_ coding:utf-8 _*_
__author__ = 'YL007'
__date__ = '2018/7/14 17:24'
import xadmin

from .models import UserMessage, UserAsk, UserCourse, UserFavorite, CourseComments

class UserAskAdmin(object):
    list_display = ['name', 'mobile','course_name', 'add_time']
    search_fields = ['name', 'mobile','course_name']
    list_filter = ['name', 'mobile','course_name', 'add_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']


class UserMessageAdmin(object):
    list_display = ['name', 'message', 'has_read', 'add_time']
    search_fields = ['name', 'message', 'has_read']
    list_filter = ['name', 'message', 'has_read', 'add_time']


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments', 'add_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'course', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'course', 'fav_id', 'fav_type']
    list_filter = ['user', 'course', 'fav_id', 'fav_type', 'add_time']

xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
