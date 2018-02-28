from django.contrib import admin

from apirest.models import Cocktail, Ingredient


class CocktailAdmin(admin.ModelAdmin):
    list_display = ('name', )
    ordering = ('name',)

admin.site.register(Cocktail, CocktailAdmin)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', )
    ordering = ('name',)

admin.site.register(Ingredient, IngredientAdmin)
