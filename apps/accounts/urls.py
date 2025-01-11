from django.urls import path

from apps.accounts import views

app_name = 'accounts'

urlpatterns = [
    path('user/edit/', views.ProfileUpdateView.as_view(), name='profile_edit'),
    path('user/<slug:slug>/', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]