from django.contrib import admin
from .models import Recipe

# admin.site.register(Recipe)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):

    list_display = ('name', 'describe','ingredients', 'steps')
    # list_display_links = ('name')
    # search_fields = ('name')
    # list_filter = ('describe')
# Register your models here.
