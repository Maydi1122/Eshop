from django.contrib import admin

# Register your models here.
from .models import profile

class profileAdmin(admin.ModelAdmin):
    class meta:
        model = profile

admin.site.register(profile,profileAdmin)

