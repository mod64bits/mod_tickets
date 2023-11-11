from django.db import models

from apps.base.models import BaseModel


class Company(BaseModel):
    name = models.CharField('Nome', max_length=100)
    document = models.CharField('Documento', max_length=35, null=True, blank=True)
    email = models.EmailField("Email", null=True, blank=True)
    phone = models.CharField('Telefone', max_length=20)

    def __str__(self):
        return self.name
