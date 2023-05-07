import uuid as uuid
from django.db import models
from utils.modules import path_and_rename


class User(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4(), editable=True)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField()
    avatar = models.ImageField(upload_to=path_and_rename('users'), null=True, blank=True, default=None)
    otp = models.CharField(max_length=6, null=True, blank=True, default=None)
    otp_expire_at = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.phone_number} {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "users"
        verbose_name_plural = "users"
        db_table = "users"


