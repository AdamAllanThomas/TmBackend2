from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task
from projects.models import Project


@receiver(post_save, sender=Task)
def update_project_status(sender, instance, **kwargs):
    project = instance.project
    tasks = Task.objects.filter(project=project)

    if all(task.status == "Completed" for task in tasks):
        project.status = "Completed"
    elif any(task.status == "In Progress" for task in tasks):
        project.status = "In Progress"
    else:
        project.status = "Not Started"

    project.save()
