from django.db import models
from apps.base.models import BaseModel
from apps.category.models import Category
from apps.category.constant import CategoryType


class Transaction(BaseModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    note = models.TextField(null=True, blank=True)
    transaction_type = models.CharField(choices=CategoryType.choice())

    def __str__(self):
        return f"{self.created_by} - {self.transaction_type} | {self.amount}"

    class Meta:
        db_table = 'transaction'
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'
        ordering = ['-created_at']
