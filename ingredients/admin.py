from django.contrib import admin
from ingredients.models import Category, Ingredient, Uptostock, InToStock, PickUp

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Uptostock)
admin.site.register(InToStock)
admin.site.register(PickUp)
