"""AMRY URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
# from user import views as user_view
from django.contrib.auth import views as auth




urlpatterns = [
    path('admin/', admin.site.urls), 
    path('signup',views.signup,name='signup'),
    path('',views.Login,name='login'),
    # path('logout', auth.LogoutView.as_view(template_name ='login.html'), name ='Logout'),
    path('logout',views.logout, name='logout'),
    path('success', views.success, name='success'),
    path('plane', views.plane, name='plane'),
    path('road', views.road, name='road'),
    path('building', views.building, name='building'),
    path('home',views.index,name='home')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
