from django.contrib import admin
from .models import Post , Category
from django.template.defaultfilters import truncatewords
# Register your models here.
admin.site.register(Category)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_category' , 'get_description',)
    prepopulated_fields = {'slug': ('title',)}

    def get_description(self, obj):
        return truncatewords(obj.content, 2)

    get_description.short_description = "content"