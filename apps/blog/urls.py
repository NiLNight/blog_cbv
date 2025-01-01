from django.urls import path
from apps.blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
]