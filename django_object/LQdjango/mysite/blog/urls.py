from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blog_title, name='blog_title'),#name在HTML模板中配合项目url下的指向这里的namespace使用
    url(r'(?P<article_id>\d)/$', views.blog_article, name='blog_detail'),
]