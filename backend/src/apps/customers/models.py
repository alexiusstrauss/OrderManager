from django.db import models


class Customer(models.Model):
    """
    Modelo para representar um cliente.

    Campos:
        - name (str): Nome completo do cliente.
        - email (str): Email do cliente único e obrigatório.
        - created_at (datetime): Data de criação da conta.

    Atributos especiais:
        - __str__: Retorna a representação em string do nome do cliente.

    Meta-dados:
        - verbose_name: Nome singular do modelo para uso em formulários e listagens.
        - verbose_name_plural: Nome plural do modelo para uso em formulários e listagens.
    """

    name = models.CharField(verbose_name="Nome completo", max_length=120, blank=False)
    email = models.EmailField(verbose_name="Email", blank=False, unique=True)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        """
        Meta-dados do modelo Cliente.

        Nome singular e plural para uso em formulários e listagens.
        """

        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Partner(models.Model):
    """
    Modelo para representar um parceiro.

    Campos:
        - customer (OneToOneField): O cliente associado a esse parceiro.
        - activate (bool): Indica se o parceiro está ativo ou não.
        - create_at (datetime): Data de criação da conta do parceiro.

    Atributos especiais:
        - __str__: Retorna uma string que representa o nome do parceiro e o estado de atividade.

    Meta-dados:
        - verbose_name: Nome singular do modelo para uso em formulários e listagens.
        - verbose_name_plural: Nome plural do modelo para uso em formulários e listagens.
    """

    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='partner')
    activate = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} - Active: {self.activate}"

    class Meta:
        """
        Meta-dados do modelo Parceiro.

        Nome singular e plural para uso em formulários e listagens.
        """

        verbose_name = "Parceiro"
        verbose_name_plural = "Parceiros"
