from django.contrib import admin
from ninek_site.models import Category, Page, About
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category)
admin.site.register(Page)
admin.site.register(About)
