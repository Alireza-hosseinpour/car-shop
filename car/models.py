import uuid as uuid

from django.db import models

from user.models import User
from utils.modules import path_and_rename


class Category(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4())
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'


class Car(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    brand = models.CharField(max_length=20, null=False, blank=False)
    color = models.CharField(max_length=20, null=True, blank=True)
    price = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=path_and_rename('cars'), null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.brand} {self.name}'


class Purchase(models.Model):
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    purchase_date = models.DateTimeField(null=True)
    is_delivered = models.BooleanField(null=False, default=False)
    is_paid = models.BooleanField(null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
