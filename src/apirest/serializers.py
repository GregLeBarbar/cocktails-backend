# -*- coding:utf-8 -*-
from rest_framework import serializers
from apirest.models import Cocktail, Ingredient


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'quantity')


class CocktailSerializer(serializers.ModelSerializer):

    ingredients = IngredientSerializer(source='ingredient_set', many=True, read_only=False)

    class Meta:
        model = Cocktail
        fields = ('id', 'name', 'image', 'description', 'ingredients')

    def create(self, validated_data):
        # extract ingredients data
        ingredients_data = validated_data.pop('ingredient_set')

        # create cocktail without ingredients
        cocktail = Cocktail.objects.create(**validated_data)

        # for each ingredient, create it and add it to cocktail
        for ingredient in ingredients_data:
            Ingredient.objects.create(
                name=ingredient["name"],
                quantity=ingredient["quantity"],
                cocktail=cocktail
            )

        return cocktail

    def update(self, cocktail, validated_data):

        if 'ingredient_set' in validated_data:
            ingredients_data = validated_data.pop('ingredient_set')

            if ingredients_data:
                for ingredient_data in ingredients_data:
                    ingredient_exist = False
                    for ingredient in cocktail.ingredient_set.all():
                        if ingredient_data['name'] == ingredient.name:
                            ingredient_exist = True
                            ingredient.quantity = ingredient_data['quantity']
                            ingredient.save()
                    if ingredient_exist is False:
                        ingredient = Ingredient.objects.create(
                            name=ingredient_data['name'],
                            quantity=ingredient_data['quantity'],
                            cocktail=cocktail
                        )

        Cocktail.objects.filter(pk=cocktail.pk).update(**validated_data)

        cocktail = Cocktail.objects.get(pk=cocktail.pk)

        return cocktail
