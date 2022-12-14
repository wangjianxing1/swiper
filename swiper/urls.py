"""swiper URL Configuration

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

import user.api
import social.api

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('user/verify_code', user.api.get_verify_code),
    path('user/login', user.api.login),
    path('user/profile', user.api.get_profile),
    path('user/modify_profile', user.api.modify_profile),
    path('user/avater/uploads', user.api.upload_avatar),

    path('social/users', social.api.get_users),
    path('social/like', social.api.like),
    path('social/superlike', social.api.superlike),
    path('social/dislike', social.api.dislike),
    path('social/rewind', social.api.rewind),
    path('social/friends', social.api.friends),

]
