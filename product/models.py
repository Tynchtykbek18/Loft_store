from django.db import models

# Create your models here.
class Product(models.Model):
    pr_name = models.TextField(verbose_name='наименование товара')
    category = models.TextField(verbose_name='категория товара')
    description = models.TextField(verbose_name='описание товара')
    price = models.DecimalField(verbose_name='цена товара', max_digits=10, decimal_places=3, default=0)
    quantity = models.IntegerField(verbose_name='количество на складе')

    def __str__(self):
        return self.pr_name


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

