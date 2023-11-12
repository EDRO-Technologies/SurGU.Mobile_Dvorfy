from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



class User(models.Model):
    name = models.CharField("Имя пользователя",max_length=30)
    email = models.EmailField("Email",max_length=100)
    password = models.TextField("Пароль пользователя")
    task = models.TextField("Задание")
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.TextField("Задание")
    description = models.TextField("Описание")
    users = models.TextField("Выполняющй")
    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"

class groups(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    id = models.AutoField(primary_key = True, unique = True)
    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"

class message(models.Model):
    id = models.AutoField(primary_key = True, unique = True)
    datetime = models.TimeField("Время")
    addressee = models.CharField("Отправитель" ,max_length=30, null = True)
    destination = models.CharField("Получатель",max_length=30)
    content = models.TextField("Содержание")
    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"
