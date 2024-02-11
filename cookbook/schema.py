import graphene
from graphene_django import DjangoObjectType
from django.core.exceptions import ObjectDoesNotExist
from ingredients.models import Category, Ingredient, Uptostock, InToStock, PickUp


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "size", 'quantity',
                  'color', 'shipped', 'created_at')


class UptostockType(DjangoObjectType):
    class Meta:
        model = Uptostock
        fields = ("id", "ingredient", "other_fields")


class InToStockType(DjangoObjectType):
    class Meta:
        model = InToStock
        fields = ("id", "name", "size", "color", "quantity", "created_at")


class PickUpType(DjangoObjectType):
    class Meta:
        model = PickUp
        fields = ("id", "name", "size", "color", "quantity", "created_at")


class CreateUptostock(graphene.Mutation):
    class Arguments:
        ingredient_id = graphene.Int(required=True)

    uptostock = graphene.Field(UptostockType)

    def mutate(self, info, ingredient_id, **kwargs):
        uptostock = Uptostock.create_and_save(ingredient_id, **kwargs)
        return CreateUptostock(uptostock=uptostock)


class CreateInToStock(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        size = graphene.String(required=True)
        color = graphene.String(required=True)
        quantity = graphene.Int(required=True)

    into_stock = graphene.Field(InToStockType)

    def mutate(self, info, name, size, color, quantity):
        into_stock = InToStock(name=name, size=size,
                               color=color, quantity=quantity)
        into_stock.save()
        return CreateInToStock(into_stock=into_stock)


class CreatePickUp(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        size = graphene.String(required=True)
        color = graphene.String(required=True)
        quantity = graphene.Int(required=True)

    pick_up = graphene.Field(PickUpType)

    def mutate(self, info, name, size, color, quantity):
        pick_up = PickUp(name=name, size=size,
                         color=color, quantity=quantity)
        pick_up.save()
        return CreatePickUp(pick_up=pick_up)


class CreateIngredient(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        notes = graphene.String()
        size = graphene.String(required=True)
        quantity = graphene.Int(required=True)
        color = graphene.String(required=True)

    ingredient = graphene.Field(IngredientType)

    def mutate(self, info, name, notes, size, quantity, color):
        try:
            ingredient = Ingredient(
                name=name, notes=notes, size=size, quantity=quantity, color=color)
            ingredient.save()
        except Exception as e:
            print(f"Error creating ingredient: {e}")
            raise

        return CreateIngredient(ingredient=ingredient)


class UpdateIngredient(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        notes = graphene.String()
        size = graphene.String()
        quantity = graphene.Int()
        color = graphene.String()

    ingredient = graphene.Field(IngredientType)

    def mutate(self, info, id, name, notes, size=None, quantity=None, color=None):
        try:
            ingredient = Ingredient.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise Exception("Ingredient not found")
        ingredient.name = name
        ingredient.notes = notes
        if size is not None:
            ingredient.size = size
        if quantity is not None:
            ingredient.quantity = quantity
        if color is not None:
            ingredient.color = color
        ingredient.save()
        return UpdateIngredient(ingredient=ingredient)


class DeleteIngredient(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ingredient = graphene.Field(IngredientType)

    def mutate(self, info, id):
        try:
            ingredient = Ingredient.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise Exception("Ingredient not found")
        ingredient.delete()
        return DeleteIngredient(ingredient="ingredient deleted")


class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
    category = graphene.Field(lambda: CategoryType)

    def mutate(self, info, name):
        category = Category(name=name)
        category.save()
        return CreateCategory(category=category)


class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    total_last_24_hours = graphene.Int()
    ingredients_last_24_hours = graphene.List(IngredientType)
    all_uptostocks = graphene.List(UptostockType)
    all_into_stocks = graphene.List(InToStockType)
    all_pick_ups = graphene.List(PickUpType)

    def resolve_all_ingredients(self, info):
        return Ingredient.objects.all()

    def resolve_total_last_24_hours(self, info):
        return Ingredient.calculate_total_last_24_hours()

    def resolve_ingredients_last_24_hours(self, info):
        return Ingredient.objects.last_24_hours()

    def resolve_all_uptostocks(self, info):
        return Uptostock.objects.all()

    def resolve_all_into_stocks(self, info):
        return InToStock.objects.all()

    def resolve_all_pick_ups(self, info):
        return PickUp.objects.all()


class ShipOutIngredient(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        size = graphene.String(required=True)
        color = graphene.String(required=True)

    total_quantity = graphene.Int()

    def mutate(self, info, name, size, color):
        total_quantity = Ingredient.shipout(name, size, color)

        return ShipOutIngredient(total_quantity=total_quantity)


class UpdateIngredientQuantity(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        size = graphene.String(required=True)
        color = graphene.String(required=True)
        quantity = graphene.Int(required=True)

    ingredient = graphene.Field(IngredientType)

    def mutate(self, info, name, size, color, quantity):
        try:
            ingredient = Ingredient.objects.get(
                name=name, size=size, color=color)
        except ObjectDoesNotExist:
            raise Exception("Ingredient not found")

        if quantity < 0 or quantity > ingredient.quantity:
            raise Exception("Invalid quantity")

        ingredient.quantity -= quantity
        ingredient.save()

        return UpdateIngredientQuantity(ingredient=ingredient)


class Mutation(graphene.ObjectType):
    create_ingredient = CreateIngredient.Field()
    update_ingredient = UpdateIngredient.Field()
    delete_ingredient = DeleteIngredient.Field()
    ship_out_ingredient = ShipOutIngredient.Field()
    update_ingredient_quantity = UpdateIngredientQuantity.Field()
    create_into_stock = CreateInToStock.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
