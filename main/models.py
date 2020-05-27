from django.db import models
from django.urls import reverse

# Create your models here.
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=32, db_index=True)
    slug = models.SlugField(max_length=48, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product-list', args=[self.slug])


class ActiveManager(models.Manager):
    def active(self):
        return self.filter(active=True)


class Product(models.Model):
    name = models.CharField(max_length=32, db_index=True)
    weight1 = models.DecimalField(max_digits=7, decimal_places=3)
    weight2 = models.DecimalField(max_digits=7, decimal_places=3)
    slug = models.SlugField(max_length=48, unique=True, db_index=True)
    image = models.ImageField(upload_to="product-images")
    thumbnail = models.ImageField(upload_to="product-thumbnails", null=True)
    active = models.BooleanField(default=True)
    objects = ActiveManager()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,)
    date_added = models.DateTimeField(auto_now_add=True,)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product-detail', args=[self.id, self.slug])


class CatalogPdf(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=48, unique=True,)
    pdf = models.FileField(upload_to='pdf-files')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:catalog', args=[self.slug])


class Rates(models.Model):
    goldRate = models.DecimalField(max_digits=8, decimal_places=2)
    silverRate = models.DecimalField(max_digits=8, decimal_places=2)
    date_added = models.DateTimeField(auto_now=True,)

