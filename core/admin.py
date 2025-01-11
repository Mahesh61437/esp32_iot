from django.contrib import admin
from .models import ServoConfig, ActionLog, DeviceHealth

# Register ServoConfig model for editing schedules
@admin.register(ServoConfig)
class ServoConfigAdmin(admin.ModelAdmin):
    list_display = ("action_name", "time_to_run", "speed", "hour", "minute")
    list_editable = ("time_to_run", "speed", "hour", "minute")
    search_fields = ("action_name",)

# Register ActionLog model for viewing logs
@admin.register(ActionLog)
class ActionLogAdmin(admin.ModelAdmin):
    list_display = ("action_name", "status", "timestamp")
    list_filter = ("action_name", "status")
    search_fields = ("action_name",)

# Register DeviceHealth model for monitoring health
@admin.register(DeviceHealth)
class DeviceHealthAdmin(admin.ModelAdmin):
    list_display = ("date", "status", "last_seen")
    list_filter = ("status",)
    search_fields = ("status",)
