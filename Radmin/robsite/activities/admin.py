from django.contrib import admin

from .models import Activity, OneTimeActivity

admin.site.register(Activity)
admin.site.register(OneTimeActivity)