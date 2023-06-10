from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    username = models.CharField(blank=False, max_length=50, unique=True)
    password = models.CharField(blank=False, max_length=50)
    first_name = models.CharField(blank=False, max_length=50)
    last_name = models.CharField(blank=False, max_length=50)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(blank=False, null=True, max_length=254)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_staff": self.is_staff,
            "email": self.email,
        }


class Category(models.Model):
    name = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=500)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "imageUrl": self.imageUrl
        }


class Dish(models.Model):
    name = models.CharField(blank=False, max_length=200)
    price = models.IntegerField(blank=False)
    description = models.CharField(blank=False, max_length=500)
    imageUrl = models.CharField(blank=False, max_length=500)
    is_gluten_free = models.BooleanField(default=False)
    is_vegeterian = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "imageUrl": self.imageUrl,
            "is_gluten_free": self.is_gluten_free,
            "is_vegeterian": self.is_vegeterian,
            "category": self.category.name
        }


class Delivery(models.Model):
    is_delivered = models.BooleanField(default=False)
    address = models.CharField(blank=False, max_length=200)
    notes = models.CharField(max_length=500)
    created = models.DateTimeField(null=True)

    def serialize(self):
        return {
            "id": self.id,
            'is_delivered': self.is_delivered,
            'address': self.address,
            'notes': self.notes,
            'created': self.created
        }


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery = models.OneToOneField(
        Delivery, on_delete=models.CASCADE, primary_key=True)

    def serialize(self):
        return {
            "id": self.id,
            'user': self.user.id,
            'items': [item.serialize() for item in self.items_set.all()],
            'delivery': self.delivery.id,
        }


class Items(models.Model):
    dish = models.ForeignKey(
        Dish, on_delete=models.CASCADE)
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    def serialize(self):
        return {
            "id": self.id,
            'dish': self.dish.serialize(),
            'cart': self.cart.user_id,
            'amount': self.amount,
        }
