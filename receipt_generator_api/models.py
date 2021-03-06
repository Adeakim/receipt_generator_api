from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
import uuid
import datetime
from phonenumber_field.modelfields import PhoneNumberField

class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)
        user = self.models(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password, **extra_fields):

        user = self.model(email=self.normalize_email(email))
        user.name = name
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True

        user.save(using=self._db)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        unique=True, primary_key=True, default=uuid.uuid4, editable=False
    )
    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    mobile_number = PhoneNumberField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("name",)

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email

class Receipt(models.Model):

    id = models.UUIDField(
        unique=True, primary_key=True, default=uuid.uuid4, editable=False
    )
    user = models.ForeignKey(User,null=True,to_field='email',on_delete=models.CASCADE)
    email = models.EmailField(null=True, max_length=255)
    name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null =True)
    mobile_number = PhoneNumberField(null=True)
    total_amount_payable=models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
