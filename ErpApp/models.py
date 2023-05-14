from django.db import models
from django.utils.text import slugify
from utils.generate_code import generate_code
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    image=models.ImageField( upload_to='Category')
    def __str__(self):
        return self.name
    

STATUS = [
        ('Available', 'Available'),
        ('Sold', 'Sold'),
        ('Returns', 'Returns'),
    ]
COLORS=[('Black','Black'),('Grey','Grey'),('White','White'),('Blue','Blue'),('Brown','Brown'),('Red','Red')]

class Item(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to='Items')
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(
        max_digits=10, decimal_places=2,default=0)
    price_sales = models.DecimalField(
        max_digits=10, decimal_places=2,default=0)
    code = models.CharField(max_length=50,default=generate_code)
    details = models.TextField(max_length=500)
    active = models.BooleanField(default=True)
    status = models.CharField(
        max_length=50, choices=STATUS)
    colors = models.CharField(
        max_length=50, choices=COLORS)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='Item_Category')
    slug=models.SlugField(null=True,blank=True)
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):  # new
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)