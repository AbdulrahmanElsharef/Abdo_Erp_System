from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Item(models.Model):
    status_item = [
        ('Available', 'Available'),
        ('Sold', 'Sold'),
        ('Soon', 'Soon'),
    ]
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=150)
    item_img = models.ImageField(
        upload_to='item_images', null=True, blank=True)
    brand_img = models.ImageField(
        upload_to='brand_images', null=True, blank=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(
        max_digits=10, decimal_places=2)
    Color = models.CharField(max_length=50, null=True, blank=True)
    details = models.TextField(max_length=500, null=True, blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(
        max_length=50, choices=status_item, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='Category')

    def __str__(self):
        return self.name
