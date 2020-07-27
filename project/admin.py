from django.contrib import admin
from project.models import Activity, Icon, ActivityMonth, Calendar, Owner
# Register your models here.

admin.site.register(Owner)
admin.site.register(Calendar)
admin.site.register(Activity)
admin.site.register(ActivityMonth)
admin.site.register(Icon)