from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from common.models import BaseModel
from accounts.managers import BaseUserManager
from django.db import models


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(blank=False, null=False, unique=True, verbose_name='почтовый адрес')
    password = models.CharField(max_length=128, blank=True, null=True, verbose_name='пароль')
    is_staff = models.BooleanField(default=False, blank=True, verbose_name='сотрудник')
    is_active = models.BooleanField(default=False, blank=True, verbose_name='активный')

    USERNAME_FIELD = 'email'

    objects = BaseUserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'usr'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('created_at',)