from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.CustomUserListCreateView.as_view(), name="user-list-create"),
    path(
        "users/<int:pk>",
        views.CustomUserRetrieveUpdateDestroyView.as_view(),
        name="user-retrieve-update-destroy",
    ),
    path(
        "users/profile/update/",
        views.UserProfileUpdateView.as_view(),
        name="user-profile-update",
    ),
    path(
        "users/change-password/",
        views.ChangePasswordView.as_view(),
        name="user-change-password",
    ),
    path("users/register/", views.UserRegistrationView.as_view(), name="user-register"),
    path("users/me/", views.UserProfileUpdateView.as_view(), name="user-me"),
]
