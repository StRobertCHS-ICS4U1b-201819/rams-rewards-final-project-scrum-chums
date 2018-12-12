from django.contrib import admin

from .models import Activity, OneTimeActivity, RepeatedActivity, Student

admin.site.register(Activity)
admin.site.register(RepeatedActivity)
admin.site.register(OneTimeActivity)
admin.site.register(Student)

#class StudentAdmin(admin.ModelAdmin):



