from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
User = get_user_model()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_%(class)s_set"
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="updated_%(class)s_set"
    )
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        abstract = True
