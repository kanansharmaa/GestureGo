"""GestureGo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/login', permanent=False)),
    
    path('admin/', admin.site.urls),
    path('home/',views.home,name="home"),
   
    path('translation/',views.translation,name="translation"),
    path('menu/', views.menu, name='menu'),
    path('home/signtospeech/',include('SignToSpeech.urls')),
    path('text_to_speech/',views.text_to_speech,name="text_to_speech"),

    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerUser,name="register"),
    path('privacy/',views.privacy,name="privacy"),
     path('asl/',views.asl,name="asl"),
    
]
