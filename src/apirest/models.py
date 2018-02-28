from django.db import models


class Cocktail(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return "{}".format(self.name)


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.SmallIntegerField()
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)
