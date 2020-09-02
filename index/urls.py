from django.urls import path
from index import views

urlpatterns = [
    path('search', views.search),
    path('h', views.h),
    path('upload', views.upload),
    path("device", views.get_device),
    path('command', views.command),
    path('qrcode', views.erweima)
]
