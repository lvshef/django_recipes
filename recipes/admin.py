from django.contrib import admin
from .models import Recipe, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
