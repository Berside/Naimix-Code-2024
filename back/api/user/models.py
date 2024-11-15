from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, data: dict):
        user = self.model(**data)
        user.set_password(data['password'])
        user.save(using=self._db)
        return user

    def create_superuser(self, data: dict):
        user = self.create_user(data)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    birthdate = models.DateTimeField(null=True, blank=True)
    birth_country = models.CharField(max_length=100, null=True, blank=True)
    birth_city = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

    def get_short_name(self):
        return self.first_name
    