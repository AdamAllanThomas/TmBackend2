from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ("user", "User"),
        ("admin", "Admin"),
    ]

    phone = models.CharField(max_length=15, blank=False, null=False, default="")
    name = models.CharField(max_length=255, blank=False, null=False, default="")
    profile_image = models.ImageField(
        upload_to="profile_images/", null=True, blank=True
    )
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default="User")
    street_address = models.CharField(max_length=255, blank=False, null=False)
    city = models.CharField(max_length=20, blank=False, null=False)
    state = models.CharField(max_length=2, blank=False, null=False)
    country = models.CharField(max_length=20, blank=False, null=False)
    postal_code = models.CharField(max_length=7, blank=False, null=False)
