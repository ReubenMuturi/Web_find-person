"""
URL configuration for my_projects project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from profiles import views  # Import your views from the profiles app

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin route
    path('accounts/', include('django.contrib.auth.urls')),  # Login-related routes
    path('profiles/', include('profiles.urls')),  # Your profiles app URLs

    # Add this line for the homepage
    path('', views.home, name='home'),  # This will map the root path to the 'home' view
]
