from django.urls import path

from apps.accounts import views

app_name = 'accounts'

urlpatterns = [
    path('user/edit/', views.ProfileUpdateView.as_view(), name='profile_edit'),
    path('user/<slug:slug>/', views.ProfileDetailView.as_view(), name='profile_detail'),
]