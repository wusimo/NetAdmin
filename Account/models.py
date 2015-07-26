import json
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):

        """
        Creates and saves a User with the given email, username and password.
        """

        if not email:
            raise ValueError('Users must have a vaild email address')

        if not kwargs.get('username'):
            raise ValueError('Users must have a vaild username')

        if not kwargs.get('campus'):
            raise ValueError('Users must choose a vaild campus')

        account = self.model(
            email=self.normalize_email(email), username=kwargs.get('username')
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.save()

        return account


class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)

    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_parents = models.BooleanField(default=False)
    is_TA = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'campus']

    def __unicode__(self):
        return self.email

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        # Simplest possible answer: All admins are staff
        return self.is_admin
