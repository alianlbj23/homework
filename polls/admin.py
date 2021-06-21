from django.contrib import admin
from .models import Post, Country, City

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

admin.site.register(Post, PostAdmin)
admin.site.register(Country)
admin.site.register(City)
# Register your models here.
