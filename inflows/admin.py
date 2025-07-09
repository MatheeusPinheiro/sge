from django.contrib import admin
from . import models
# Register your models here.
class InflowAdmin(admin.ModelAdmin):
    list_display = ("supplier", "product", "quantity", "created_at", "updatet_at")
    search_fields = ("supplier__name", "product__title")

admin.site.register(models.Inflow, InflowAdmin)