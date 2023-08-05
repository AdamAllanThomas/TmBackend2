from django.conf import settings
from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ("New", "New"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]

    PRIORITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    dueDate = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="New")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="Low")
    assignedTo = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="tasks_assigned",
    )
