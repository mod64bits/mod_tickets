from django.db import models

from apps.base.models import BaseModel
from apps.companies.models import Company
from apps.users.models import User


class Ticket(BaseModel):
    STATUS = (
        ('OPEN', 'Aberto'),
        ('IN_SERVICE', 'Em atendimento'),
        ('CLOSED', 'Encerrado'),
        ('CANCELED', 'Cancelado')
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        verbose_name='Empresa',
        related_name='ticket_company',
        null=True,
        blank=True
    )
    name = models.CharField('Nome', max_length=100)
    department = models.CharField('Departamento', max_length=100)
    responsible = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='responsible_tick',
        editable=False
    )
    started_in = models.DateTimeField(null=True, blank=True, editable=False)
    status = models.SmallIntegerField(
        choices=STATUS, default='OPEN', editable=False)
    closed_in = models.DateTimeField(null=True, blank=True, editable=False)

    def __str__(self):
        return self.name
