import uuid

from django.db import models
from users.models import CustomUser

# Create your models here.
class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='orders')
    created = models.DateTimeField(verbose_name='Дата заказа', auto_now_add=True, blank=True)
    total_cost = models.FloatField(verbose_name='Сумма заказа', blank=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'



class ProductsInOrder(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='customer')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Товар', related_name='order')
    quantity = models.IntegerField(verbose_name='Сумма заказа', blank=True)

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'