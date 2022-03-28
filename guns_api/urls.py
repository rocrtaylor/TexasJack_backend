from django.urls import path
from . import views

urlpatterns = [
  path('api/guns', views.GunList.as_view(), name='gun_list'),
  path('api/guns/<int:pk>', views.GunDetail.as_view(), name='gun_detail'),
]