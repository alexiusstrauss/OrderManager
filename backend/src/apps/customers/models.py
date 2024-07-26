from django.db import models


class Customer(models.Model):
    name = models.CharField(verbose_name="Nome completo", max_length=120, blank=False)
    email = models.EmailField(verbose_name="Email", blank=False, unique=True)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Partner(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='partner')
    activate = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} - Active: {self.activate}"

    class Meta:
        verbose_name = "Parceiro"
        verbose_name_plural = "Parceiros"
