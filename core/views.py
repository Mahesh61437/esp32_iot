from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
from django.http import JsonResponse
from .models import ServoConfig, ActionLog, DeviceHealth

@csrf_exempt
def get_schedules(request):
    schedules = list(ServoConfig.objects.values(
        "action_name", "time_to_run", "speed", "hour", "minute"
    ))
    return JsonResponse({"schedules": schedules})

@csrf_exempt
def log_action_status(request):
    if request.method == "POST":
        action_name = request.POST.get("action_name")
        status = request.POST.get("status") == "true"

        if action_name:
            ActionLog.objects.create(action_name=action_name, status=status)
            return JsonResponse({"message": "Action status logged successfully"})
        else:
            return JsonResponse({"error": "Invalid action name"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def update_device_health(request):
    if request.method == "POST":
        status = request.POST.get("status", "unknown")
        DeviceHealth.objects.update_or_create(
            date=now().date(),
            defaults={"status": status, "last_seen": now()}
        )
        return JsonResponse({"message": "Device health updated successfully"})

    return JsonResponse({"error": "Invalid request method"}, status=405)

def get_action_logs(request):
    logs = list(ActionLog.objects.values("action_name", "status", "timestamp"))
    return JsonResponse({"logs": logs})

def get_device_health(request):
    health = list(DeviceHealth.objects.values("date", "status", "last_seen"))
    return JsonResponse({"health": health})


def device_health_and_logs_page(request):
    return render(request, 'core/health_and_logs.html')

