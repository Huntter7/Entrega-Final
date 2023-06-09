"""Controles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Kepler.views import (index, PostList, PostDetail, PostCreate, 
                                PostUpdate, PostDelete, SignUp, Login, 
                                Logout, ProfileUpdate, MensajeCreate, MensajeDelte, MensajeList,
                                ProfileDetail, ProfileList, ProfileCreate, about)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
    path('posteo/list', PostList.as_view(), name='post-list'),
    path('posteo/<pk>/detail', PostDetail.as_view(), name='post-detail'),
    path('posteo/create', PostCreate.as_view(), name='post-create'),
    path('posteo/<pk>/update', PostUpdate.as_view(), name='post-update'),
    path('posteo/<pk>/delete', PostDelete.as_view(), name='post-delete'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/<pk>/update', ProfileUpdate.as_view(), name='profile-update'),
    path('profile/<pk>/view', ProfileDetail.as_view(), name='profile-detail'),
    path('profile/list', ProfileList.as_view(), name='profile-list'),
    path('profile/create', ProfileCreate.as_view(), name='profile-create'),
    path('mensaje/create', MensajeCreate.as_view(), name='mensaje-create'),
    path('mensaje/list', MensajeList.as_view(), name='mensaje-list'),
    path('mensaje/<pk>/delete', MensajeDelte.as_view(), name='mensaje-delete'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
