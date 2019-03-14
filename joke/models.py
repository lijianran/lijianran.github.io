from django.db import models


class Person(models.Model):
    SEX = (
        ('male', '男性'),
        ('female', '女性')
    )
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=32)
    sex = models.CharField(max_length=8, choices=SEX)
    age = models.IntegerField()
    city = models.CharField(max_length=16)
    description = models.TextField()


class Article(models.Model):
    title = models.CharField(max_length=16)
    sub_title = models.CharField(max_length=16)
    date = models.DateField(auto_now_add=True)
    text = models.TextField()
    auth = models.ForeignKey(Person, on_delete=models.CASCADE)
