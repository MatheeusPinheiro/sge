from django.contrib import admin
from . import models
# Register your models here.
class CategorieAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)

admin.site.register(models.Category, CategorieAdmin)