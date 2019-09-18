from django.contrib import admin

from cash.models import Activity, Saving


class ActivityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Activity._meta.get_fields()]


admin.site.register(Activity, ActivityAdmin)

admin.site.register(Saving)
