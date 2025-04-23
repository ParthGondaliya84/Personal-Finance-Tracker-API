from django.db import models
from apps.base.models import BaseModel
from apps.category.constant import CategoryType


class Category(BaseModel):
    title = models.CharField(max_length=50)
    entry_type = models.CharField(choices=CategoryType.choice())

    def __str__(self):
        return f"{self.title} | {self.entry_type}"

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
