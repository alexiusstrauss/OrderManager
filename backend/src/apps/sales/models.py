from enum import Enum
from uuid import uuid4

from django.db import models
from django.utils import timezone


class ProductType(Enum):
    PHYSICAL = 1
    VIDEO = 2
    BOOK = 3


class CommissionStatus(Enum):
    PENDING = 0
    CANCELED = 1
    PAID = 2


class Agent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Agente"
        verbose_name_plural = "Agentes"


class Order(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False, verbose_name="Código de Venda")
    created_at = models.DateTimeField(default=timezone.now)
    agent = models.ForeignKey(Agent, on_delete=models.PROTECT)
    canceled = models.BooleanField(default=False)
    pay = models.BooleanField(default=False)

    def __str__(self):
        return f"Pedido #{self.uuid}"

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name="items")
    name = models.CharField(max_length=100)
    ean = models.CharField(max_length=13)
    description = models.TextField(blank=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    product_type = models.PositiveSmallIntegerField(
        choices=[(tag.value, tag.name) for tag in ProductType], default=ProductType.PHYSICAL
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Item de Pedido"
        verbose_name_plural = "Itens de Pedido"


class Commission(models.Model):
    id = models.AutoField(primary_key=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(
        choices=[(tag.value, tag.name) for tag in CommissionStatus], default=CommissionStatus.PENDING
    )

    class Meta:
        verbose_name = "Comissão"
        verbose_name_plural = "Comissões"
