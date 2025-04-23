from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.user.manager import PFTUserManager
from apps.user.constant import Gender
from apps.base.models import BaseModel


class PFTUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    gender = models.CharField(choices=Gender.choice(), default=Gender.MALE)

    created_by = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="created_user"
    )
    updated_by = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="updated_user"
    )

    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = PFTUserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "pft_user"
        verbose_name = "PFT user"
        verbose_name_plural = "PFT users"


class UserProfile(BaseModel):
    user = models.OneToOneField(
        PFTUser, on_delete=models.CASCADE, related_name='profile'
    )
    currency = models.CharField(max_length=10, default='INR')
    daily_buget_limit = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    monthly_buget_limit = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    profile_pic = models.ImageField(
        upload_to='profile_pic/', null=True, blank=True
    )

    def __str__(self):
        return self.user.email

    class Meta:
        db_table = "profile"
        verbose_name = "User profile"
        verbose_name_plural = "User profiles"
