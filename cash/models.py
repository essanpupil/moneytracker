import uuid

from django.db import models
from django.utils.timezone import now
from djmoney.models.fields import MoneyField


class Saving(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    balance = MoneyField(decimal_places=2, max_digits=17, default_currency='IDR')

    def __str__(self):
        return self.name


class Activity(models.Model):
    ACTIVITY_TYPE_CHOICES = (
        ('in', 'Income'),
        ('ex', 'Expense'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(default=now)
    name = models.CharField(max_length=255)
    value = MoneyField(decimal_places=2, max_digits=15, default_currency='IDR')
    type = models.CharField(choices=ACTIVITY_TYPE_CHOICES, max_length=2, default='ex')
    impacted_saving = models.ForeignKey(Saving, on_delete=models.CASCADE, null=True, blank=True)
    is_monthly = models.BooleanField(default=False)

    def __str__(self):
        return self.name
