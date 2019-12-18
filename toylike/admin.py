from django.contrib import admin
from .models import Blessing


# Register your models here.
class BlessingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Blessing, BlessingAdmin)
