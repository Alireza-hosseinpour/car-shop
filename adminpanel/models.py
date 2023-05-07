from django.db import models


class Admin(models.Model):
    username = models.CharField(max_length=30, unique=True, null=False, blank=False)
    password = models.CharField(max_length=32, null=False, blank=False)

    def __str__(self):
        return f'{self.username}'


