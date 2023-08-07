from django.urls import path
from . import views

urlpatterns = [
    path("tasks/", views.TaskListCreateView.as_view(), name="task-list-create"),
    path(
        "tasks/<int:pk>",
        views.TaskRetrieveUpdateDestroyView.as_view(),
        name="task-retrieve-update-destroy",
    ),
    path(
        "tasks/me/",
        views.UserTaskListCreateView.as_view(),
        name="user-task-list-create",
    ),
]
