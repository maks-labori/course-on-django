from django.contrib import admin

# Register your models here.
from goods.models import Categories,Products

# admin.site.register(Categories)
# admin.site.register(Products)

@admin.register(Categories)
class AdminCategories(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Products)
class AdminProducts(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}