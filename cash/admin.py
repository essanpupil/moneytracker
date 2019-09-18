from django.contrib import admin

from cash.models import Activity, Saving


class ActivityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Activity._meta.get_fields()]


admin.site.register(Activity, ActivityAdmin)


class SavingAdmin(admin.ModelAdmin):
    list_display = ["name", "balance"]


admin.site.register(Saving, SavingAdmin)
