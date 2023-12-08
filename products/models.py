from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone

FLAG_TYPES = (
    ('New','New'),
    ('Sale','Sale'),
    ('Features','Features')
    
)
class Product(models.Model):
    name = models.CharField(max_length=100)
    flag = models.CharField(max_length=10,choices=FLAG_TYPES)
    price = models.FloatField()
    image = models.ImageField(upload_to='product')
    sku = models.IntegerField()
    subtitle = models.TextField(max_length=400)
    description = models.TextField(max_length=50000)
    tags = TaggableManager()
    brand = models.ForeignKey('Brand',related_name = 'product_brand',on_delete=models.SET_NULL,null=True)
    
class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand')


class Review(models.Model):
    user = models.ForeignKey(User,related_name='user_review',on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,related_name='product_review',on_delete=models.CASCADE)
    review = models.TextField(max_length=500)
    rate = models.IntegerField(choices=[(i,i) for i in range(1,6)])
    created_at = models.DateTimeField(default=timezone.now)

class ProductImages(models.Model):
    product = models.ForeignKey(Product,related_name='product_image',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productimages')

