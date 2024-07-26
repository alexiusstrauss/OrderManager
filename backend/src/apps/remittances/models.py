from uuid import uuid4

from django.db import models
from django.utils import timezone
from src.apps.sales.models import Order


class Shipping(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False, auto_created=True)
    create_at = models.DateTimeField(default=timezone.now)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"Remessa ID: {self.uuid}"

    class Meta:
        verbose_name = "Remessa Envio"
        verbose_name_plural = "Remessas de envios"


class Royalty(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"Remessa de royalty ID: {self.uuid}"

    class Meta:
        verbose_name = "Remessa Royalty"
        verbose_name_plural = "Remessas de royalty"
