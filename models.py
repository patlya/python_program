from django.db import models
from django.contrib import admin
# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=200, null=True , blank=True)
    Image = models.ImageField(upload_to='practice Image')
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=100,null=True, blank=True)

class Author(models.Model):
   name = models.CharField(max_length=100)

class Book(models.Model):
   author = models.ForeignKey(Author, on_delete=models.CASCADE)
   title = models.CharField(max_length=100)   

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return f"{self.name}: ${self.price}"

class Cart(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def total_price(self):
        import pdb;pdb.set_trace()
        return sum([
            cart_item.total()
            for cart_item in CartItem.objects.filter(cart=self)
        ])

    def __str__(self):
        return f"{self.created}, ${self.total_price()}: {self.paid}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

    def total(self):
        return self.count * self.item.price

    def __str__(self):
        return f"{self.item.name}, " \
               f"${self.item.price} * {self.count} = ${self.total()}"    

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    birthday = models.DateField()

    @admin.display(ordering='first_name')
    def born_in_fifties(self):
        return 1950 <= self.birthday.year < 1960