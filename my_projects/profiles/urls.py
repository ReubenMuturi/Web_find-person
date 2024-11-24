from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

app_name = 'profiles'

urlpatterns = [
    path('profile_list/', views.profile_list, name='profile_list'),
    path('login/', LoginView.as_view(), name='login'),  # URL for login in profiles app
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('missing-persons/', views.missing_persons_list, name='missing_persons'),  # List missing persons
    path('matching-persons/', views.matching_persons_list, name='matching_persons'),  # List matching persons
    path('create-missing-profile/', views.create_missing_profile, name='create_missing_profile'),
    path('create-matching-profile/', views.create_matching_profile, name='create_matching_profile'),

]
