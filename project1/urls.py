"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [

    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('product/', include('product.urls')),
    path('content/', include('content.urls')),
    path('user/', include('user.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('hakkimizda/', views.hakkimizda, name='hakimizda'),
    path('referanslar/', views.referanslar, name='referanslar'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('error/', views.error, name='error'),


    path('category/<int:id>/<slug:slug>/', views.category_galery, name='category_galery'),
    path('product/<int:id>/<slug:slug>/', views.pictures_detail, name='pictures_detail'),
    path('content/<int:id>/<slug:slug>/', views.content_detail, name='content_detail'),
    path('menu/<int:id>', views.menu, name='menu'),

    path('search/', views.pictures_search, name='pictures_search'),
    path('search_auto/', views.pictures_search_auto, name="pictures_search_auto"),
    path('logout/', views.logout_view, name="logout_view"),
    path('login/', views.login_view, name="login_view"),
    path('signup/', views.signup_view, name="signup_view"),
    path('faq/', views.faq, name="faq"),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
