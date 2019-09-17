from django.db import models
from djmoney.models.fields import MoneyField


class Saving(models.Model):
    name = models.CharField(max_length=128)
    balance = MoneyField(decimal_places=2, max_digits=17, default_currency='IDR')

    def __str__(self):
        return self.name


class Activity(models.Model):
    ACTIVITY_TYPE_CHOICES = (
        ('in', 'Income'),
        ('ex', 'Expense'),
    )
    name = models.CharField(max_length=255)
    value = MoneyField(decimal_places=2, max_digits=15, default_currency='IDR')
    type = models.CharField(choices=ACTIVITY_TYPE_CHOICES, max_length=2, default='ex')
    impacted_saving = models.ForeignKey(Saving, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
