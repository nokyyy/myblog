from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name="home"),
    path('list', views.PostsListView.as_view(), name='post_list'),
    path('posts/<int:post_id>/', views.post_detail, name="post_detail"),
]

# getでviews.py に送る場合
# path('posts/<int:pk>/', views.post_detail, name="post_detail")