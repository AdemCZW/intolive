from django.db.models import Sum, Manager
from django.db import models
from django.utils import timezone


class IngredientManager(Manager):
    def last_24_hours(self):
        now = timezone.now()
        start_time = now - timezone.timedelta(days=1)
        return self.filter(created_at__range=(start_time, now))


class Category(models.Model):
    name = name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    SIZE_CHOICES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Extra Extra Large'),
        ('XXXL', 'Triple Extra Large'),
    )
    COLOR_CHOICES = (
        ('BLK', 'Black'),
        ('CRM', 'Cream'),
        ('OAT', 'Oat'),
        ('CML', 'Camel'),
        ('BRN', 'Brown'),
    )
    quantity = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    notes = models.TextField()
    shipped = models.BooleanField(default=False)
    size = models.CharField(max_length=4, choices=SIZE_CHOICES, default='M')
    created_at = models.DateTimeField(default=timezone.now)
    color = models.CharField(
        max_length=3, choices=COLOR_CHOICES, default='BLK')
    objects = IngredientManager()

    def __str__(self):
        return self.name

    @staticmethod
    def ship(quantity):
        # Get the total quantity of unshipped ingredients
        total = Ingredient.calculate_total()

        # Check if there are enough unshipped ingredients
        if total < quantity:
            raise ValueError('Not enough unshipped ingredients')

        # Subtract the quantity from the total
        total -= quantity

        # Get the unshipped ingredients, ordered by the oldest first
        ingredients = Ingredient.objects.filter(shipped=False).order_by('id')

        # Mark enough ingredients as shipped
        for ingredient in ingredients:
            if quantity > 0:
                ingredient.shipped = True
                ingredient.save()
                quantity -= ingredient.quantity
            else:
                break

    @staticmethod
    def calculate_total_last_24_hours():
        time_threshold = timezone.now() - timezone.timedelta(hours=24)
        return Ingredient.objects.filter(created_at__gte=time_threshold).aggregate(total=Sum('quantity'))['total']


class Uptostock(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    # ... other fields ...

    @staticmethod
    def get_unique_ingredients():
        # Get all ingredients and group them by 'color', 'name', and 'size'
        ingredients = Ingredient.objects.values(
            'color', 'name', 'size').distinct()

        return list(ingredients)

    @staticmethod
    def create_and_save(ingredient_id, **kwargs):
        ingredient = Ingredient.objects.get(id=ingredient_id)
        uptostock = Uptostock(ingredient=ingredient, **kwargs)
        uptostock.save()
        return uptostock


class InToStock(models.Model):
    SIZE_CHOICES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Extra Extra Large'),
        ('XXXL', 'Triple Extra Large'),
    )
    COLOR_CHOICES = (
        ('BLK', 'Black'),
        ('CRM', 'Cream'),
        ('OAT', 'Oat'),
        ('CML', 'Camel'),
        ('BRN', 'Brown'),
    )
    quantity = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    shipped = models.BooleanField(default=False)
    size = models.CharField(max_length=4, choices=SIZE_CHOICES, default='M')
    created_at = models.DateTimeField(default=timezone.now)
    color = models.CharField(
        max_length=3, choices=COLOR_CHOICES, default='BLK')

    def __str__(self):
        return self.name


class PickUp(models.Model):
    SIZE_CHOICES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Extra Extra Large'),
        ('XXXL', 'Triple Extra Large'),
    )
    COLOR_CHOICES = (
        ('BLK', 'Black'),
        ('CRM', 'Cream'),
        ('OAT', 'Oat'),
        ('CML', 'Camel'),
        ('BRN', 'Brown'),
    )
    quantity = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    shipped = models.BooleanField(default=False)
    size = models.CharField(max_length=4, choices=SIZE_CHOICES, default='M')
    created_at = models.DateTimeField(default=timezone.now)
    color = models.CharField(
        max_length=3, choices=COLOR_CHOICES, default='BLK')

    def __str__(self):
        return self.name
