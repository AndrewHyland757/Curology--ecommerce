from django.db import models
from django.urls import reverse


class Category(models.Model):

    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)


    class Meta:
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.name



class Product(models.Model):

    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    made_in = models.CharField(max_length=250,)
    made_with = models.CharField(max_length=250,)
    short_description = models.TextField(blank=False)
    description = models.TextField(blank=False)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='products/')


    class Meta:
        verbose_name_plural = 'products'


    def __str__(self):
        return self.title

        
    def get_absolute_url(self):
        return reverse('product-info', args=[self.slug])

