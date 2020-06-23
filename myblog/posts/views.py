from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post

# 何も入っていないrequestにhtmlを添えて返したあげる
def index(request):
    # return HttpResponse('Hello World! このページはインデックスや')
    posts = Post.objects.order_by('-published')
    return render(request, 'posts/index.html', {'posts': posts})

class PostsListView(ListView):
    model = Post
    template_name = "posts/list.html"

    # 検索機能
    def get_queryset(self):
        queryset = Post.objects.all()
        if 'query' in self.request.GET:
            qs = self.request.GET['query']
            queryset = queryset.filter(title__contains=qs)
        return queryset

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})
