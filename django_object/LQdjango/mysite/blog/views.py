from django.shortcuts import render, get_object_or_404
from .models import BlogArticles

# Create your views here.

def blog_title(request):#request这个参数不能缺少，它负责响应所有接收到的请求，必须在第一个
    blogs = BlogArticles.objects.all()  # 得到所有BlogArticles中的对象
    return render(request, 'blog/titles.html', {'blogs':blogs})

def blog_article(request, article_id):
    #article = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles, id=article_id)
    pub = article.publish
    return render(request, 'blog/content.html', {'article':article, 'publish':pub})
