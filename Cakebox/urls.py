"""Cakebox URL Configuration

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
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from cakeboxapi import views as api_views 
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("api/cakebox",api_views.CakeboxView,basename="cakebox")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('cakess/add/',views.CakeCreateView.as_view(),name='cake-add'),
    path('cakess/all/',views.CakeListView.as_view(),name='cake-list'),
    path('cakess/<int:pk>/',views.CakeDetailsView.as_view(),name="cake-details"),
    path('cakess/<int:pk>/remove',views.CakeDeleteView.as_view(),name="cake-delete"),
    path('cakess/<int:pk>/change',views.CakeEditview.as_view(),name="cake-edit"),
    path("register/",views.SignUpView.as_view(),name="register")




]+ router.urls+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
