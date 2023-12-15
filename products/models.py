from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
FLAG_TYPES = (
    ('New','New'),
    ('Sale','Sale'),
    ('Features','Features')
    
)
class Product(models.Model):
    name = models.CharField(_('name'),max_length=100)
    flag = models.CharField(_('flag'),max_length=10,choices=FLAG_TYPES)
    price = models.FloatField(_('price'))
    image = models.ImageField(_('image'),upload_to='product')
    sku = models.IntegerField(_('sku'))
    subtitle = models.TextField(_('subtitle'),max_length=400)
    description = models.TextField(_('description'),max_length=50000)
    tags = TaggableManager(_('tags'))
    brand = models.ForeignKey('Brand',verbose_name=('brand'),related_name = 'product_brand',on_delete=models.SET_NULL,null=True)
    
    slug = models.SlugField(blank=True,null=True)
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product,self).save(*args,**kwargs)
        
    def __str__(self):
        return self.name   
    
class Brand(models.Model):
    name = models.CharField(_('name'),max_length=100)
    image = models.ImageField(_('image'),upload_to='brand')
    slug = models.SlugField(blank=True,null=True)
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Brand,self).save(*args,**kwargs)
        
    def __str__(self):
        return self.name        


class Review(models.Model):
    user = models.ForeignKey(User,verbose_name=("user"),related_name='user_review',on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,verbose_name=('product'),related_name='product_review',on_delete=models.CASCADE)
    review = models.TextField(_('review'),max_length=500)
    rate = models.IntegerField(_('rate'),choices=[(i,i) for i in range(1,6)])
    created_at = models.DateTimeField(_('created_at'),default=timezone.now)

    def __str__(self):
        return f"{self.user} - {self.product} - {self.rate}"
    
    
    
    
class ProductImages(models.Model):
    product = models.ForeignKey(Product,verbose_name=('product'),related_name='product_image',on_delete=models.CASCADE)
    image = models.ImageField(_('image'),upload_to='productimages')

