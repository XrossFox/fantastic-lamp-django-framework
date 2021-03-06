"""fantastic_lamp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from holis import views
from user.views import CreateNewUser
from post.views import CreatePost, ListPost, DeletePost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.holis),
    path('user/create/', CreateNewUser.as_view()),
    path('post/new/', CreatePost.as_view()),
    path('post/all/', ListPost.as_view()),
    path('post/delete/<int:pk>/', DeletePost.as_view())
]
