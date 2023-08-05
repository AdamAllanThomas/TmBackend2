from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.CustomUserListCreateView.as_view(), name="user-list-create"),
    path(
        "users/<int:pk>",
        views.CustomUserRetrieveUpdateDestroyView.as_view(),
        name="user-retrieve-update-destroy",
    ),
]
