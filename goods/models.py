from re import VERBOSE

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import ForeignKey

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=150,unique=True,verbose_name='Название')
    slug = models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='Путь')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    

class Products(models.Model):
    name = models.CharField(max_length=150,verbose_name="Название",unique=True)
    slug = models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name="Путь")
    description = models.TextField(max_length=1000,blank=True,null=True,verbose_name="Описание")
    image = models.ImageField(verbose_name="Изображение",upload_to="goods_images",blank=True,null=True)
    amount = models.PositiveSmallIntegerField(verbose_name="Количество",default=0)
    price = models.DecimalField(verbose_name="Стоимость",default=0.00,max_digits=7,decimal_places=2)
    discount = models.PositiveSmallIntegerField(validators=[MaxValueValidator(limit_value=100),MinValueValidator(limit_value=0)],verbose_name="Скидка в %",default=0)
    category = ForeignKey(to=Categories,on_delete=models.CASCADE,verbose_name="Категория")

    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        
    def __str__(self):
        return self.name
