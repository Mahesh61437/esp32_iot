from django.db import models

class ActionChoices(models.TextChoices):
    RUN_FIRST = "run_first", "Run First Action"
    RUN_SECOND = "run_second", "Run Second Action"

class ServoConfig(models.Model):
    action_name = models.CharField(
        max_length=50,
        choices=ActionChoices.choices,
        unique=True
    )
    time_to_run = models.IntegerField()  # Time to run in milliseconds
    speed = models.FloatField()          # Speed percentage
    hour = models.IntegerField()         # Scheduled hour (24-hour format)
    minute = models.IntegerField()       # Scheduled minute

    def __str__(self):
        return f"{self.get_action_name_display()} - Time: {self.time_to_run}ms, Speed: {self.speed}% @ {self.hour:02}:{self.minute:02}"

class ActionLog(models.Model):
    action_name = models.CharField(
        max_length=50,
        choices=ActionChoices.choices
    )
    status = models.BooleanField()  # True = Successful, False = Failed
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_action_name_display()} - {'Success' if self.status else 'Failed'} @ {self.timestamp}"

class DeviceHealth(models.Model):
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50)  # e.g., "active", "offline"
    last_seen = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.date} - {self.status} (Last seen: {self.last_seen})"
