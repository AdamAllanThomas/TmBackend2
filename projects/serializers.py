from rest_framework import serializers
from tasks.models import Task
from tasks.serializers import TaskSerializer
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "description",
            "dueDate",
            "status",
            "owner",
            "tasks",
            "priority",
        ]

    def create(self, validated_data):
        tasks_data = validated_data.pop("tasks")
        project = Project.objects.create(**validated_data)
        for task_data in tasks_data:
            Task.objects.create(project=project, **task_data)
        return project
