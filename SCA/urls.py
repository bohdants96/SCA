"""
URL configuration for SCA project.

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
from django.urls import path
from SpyCat.views import SpyCatViewSet
from MissionTargets.views import MissionViewSet



urlpatterns = [
    path('admin/', admin.site.urls),
    path('spycat/', SpyCatViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('spycat/<int:pk>/', SpyCatViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('missions/', MissionViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('missions/<int:pk>/', MissionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('missions/<int:pk>/update_target/<int:target_id>/', MissionViewSet.as_view({'patch': 'update_target'})),
    path('missions/<int:pk>/assign_cat/', MissionViewSet.as_view({'patch': 'assign_cat'})),
]
