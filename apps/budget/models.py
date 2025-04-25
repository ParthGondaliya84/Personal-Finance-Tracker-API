from django.db import models
from apps.base.models import BaseModel
from apps.category.models import Category


class Budget(BaseModel):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.category} | {self.amount} - {self.created_by}"

    class Meta:
        db_table = "budget"
        verbose_name = "Budget"
        verbose_name_plural = "Budgets"
