from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.user.manager import PFTUserManager
from apps.user.constant import Gender


class PFTUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    gender = models.CharField(choices=Gender.choice(), default=Gender.MALE)

    created_by = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_user"
    )
    updated_by = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="updated_user"
    )

    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = PFTUserManager()

    def __str__(self):
        return self.email
    
    class MEta:
        db_table = "pft_user"
        verbose_name = "PFT user"
        verbose_name_plural = "PFT users"
