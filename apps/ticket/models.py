from django.db import models

from apps.base.models import BaseModel
from apps.companies.models import Company
from apps.users.models import User
from django.urls import reverse


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
    requester = models.CharField('Solicitantes', max_length=100)
    department = models.CharField('Departamento', max_length=100)
    description = models.TextField("Descrição do chamado")
    responsible = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='responsible_tick',
        editable=False
    )
    started_in = models.DateTimeField(null=True, blank=True, editable=False)
    status = models.CharField("Status", max_length=15, choices=STATUS, default='OPEN', editable=False)
    closed_in = models.DateTimeField(null=True, blank=True, editable=False)

    def __str__(self):
        return self.requester

    def get_absolute_url(self):
        return reverse('ticket:list_ticket',  kwargs={})
