from django.contrib import admin
from . import models
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "serie_number")
    search_fields = ("title",)

admin.site.register(models.Product, ProductAdmin)