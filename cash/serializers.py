from rest_framework import serializers

from cash.models import Activity


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ['timestamp', 'name', 'value', 'type', 'impacted_saving', 'is_monthly']
