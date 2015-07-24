from django.contrib import admin
from ninek_site.models import Category, Page, About, Media
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
class PageAdmin(admin.ModelAdmin):
     list_display = ('title', 'category')
     prepopulated_fields = {'slug':('title',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(About)
admin.site.register(Media)

