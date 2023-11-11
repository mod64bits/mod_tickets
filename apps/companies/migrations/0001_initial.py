# Generated by Django 4.2.7 on 2023-11-11 11:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Criado em"),
                ),
                (
                    "modified",
                    models.DateTimeField(auto_now=True, verbose_name="Modificado em"),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Nome")),
                (
                    "document",
                    models.CharField(
                        blank=True, max_length=35, null=True, verbose_name="Documento"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, verbose_name="Email"
                    ),
                ),
                ("phone", models.CharField(max_length=20, verbose_name="Telefone")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
