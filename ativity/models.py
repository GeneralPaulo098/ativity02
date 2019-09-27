from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField()

class Clients(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)


class Shopping_Cart(models.Model):
    date = models.CharField(max_length=50)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)

class Quantity(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    cart = models.ForeignKey(Shopping_Cart, on_delete=models.CASCADE)


