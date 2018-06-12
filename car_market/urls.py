
from django.contrib import admin
from django.urls import path
from cars import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', views.car_list, name='car_list'),
    path('cars/<int:car_id>/', views.car_detail, name='car_detail'),
]
