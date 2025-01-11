from django.urls import path
from . import views

urlpatterns = [
    path('api/get_schedules/', views.get_schedules, name='get_schedules'),
    path('api/log_action_status/', views.log_action_status, name='log_action_status'),
    path('api/update_device_health/', views.update_device_health, name='update_device_health'),
    path('api/get_action_logs/', views.get_action_logs, name='get_action_logs'),
    path('api/get_device_health/', views.get_device_health, name='get_device_health'),
    path('device_health_and_logs/', views.device_health_and_logs_page, name='device_health_and_logs_page'),
]
