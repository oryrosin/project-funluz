from django.contrib import admin
from project.models import Activity, Icon, Information, Month, Calendar
# Register your models here.

admin.site.register(Calendar)
admin.site.register(Month)
admin.site.register(Activity)
admin.site.register(Information)
admin.site.register(Icon)