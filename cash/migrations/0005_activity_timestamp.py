# Generated by Django 2.2.5 on 2019-09-18 00:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cash', '0004_auto_20190918_0734'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
