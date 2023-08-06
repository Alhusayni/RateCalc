"""
URL configuration for Djangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from FlatRate.views import home, policy, about, news, contact, NewsList
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage






urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path("ads.txt",
        RedirectView.as_view(url=staticfiles_storage.url("ads.txt")),
    ),
    path('policy/', policy, name='policy'),
    path('about/', about, name='about'),
    path('news/', NewsList.as_view(), name='news'),
    path('contact/', contact, name='contact'),

]
