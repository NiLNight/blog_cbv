from django.urls import path
from apps.blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/comments/create/', views.CommentCreateView.as_view(), name='comment_create'),
    path('post/tags/<str:tag>/', views.PostByTagListView.as_view(), name='post_by_tags'),
    path('category/<slug:slug>/', views.PostFromCategory.as_view(), name='post_by_category'),
]
