from django.contrib import admin
from . import models
# Register your models here.
class OutflowAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity", "created_at", "updatet_at")
    search_fields = ("product__title",)

admin.site.register(models.Outflow, OutflowAdmin)