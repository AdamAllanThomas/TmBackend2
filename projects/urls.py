from django.urls import path
from . import views

urlpatterns = [
    path(
        "projects/", views.ProjectListCreateView.as_view(), name="project-list-create"
    ),
    path(
        "projects/<int:pk>",
        views.ProjectRetrieveUpdateDestroyView.as_view(),
        name="project-retrieve-update-destroy",
    ),
    path(
        "projects/me/",
        views.UserProjectListCreateView.as_view(),
        name="user-project-list-create",
    ),
    path(
        "projects/create/",
        views.CreateProjectWithTasksView.as_view(),
        name="create-project-with-tasks",
    ),
]
