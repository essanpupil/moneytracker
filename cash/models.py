from django.db import models
from djmoney.models.fields import MoneyField


class Activity(models.Model):
    ACTIVITY_TYPE_CHOICES = (
        ('in', 'Income'),
        ('ex', 'Expense'),
    )
    name = models.CharField(max_length=255)
    value = MoneyField(decimal_places=2, max_digits=15, default_currency='IDR')
    type = models.CharField(choices=ACTIVITY_TYPE_CHOICES, max_length=2, default='ex')

    def __str__(self):
        return self.name
