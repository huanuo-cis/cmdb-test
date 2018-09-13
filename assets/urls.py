from django.urls import path
from django.views.generic import ListView

from assets import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('<int:asset_id>/', views.detail, name='detail'),
    path('index/', views.index , name='index'),
    path('assets_list/',views.AllAssets.as_view(),name='assets_list'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('addassets/', views.AddAssets.as_view(), name='addassets'),
    path('addtest/', views.addTest)
]