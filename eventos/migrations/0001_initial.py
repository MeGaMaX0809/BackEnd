# Generated by Django 4.1 on 2024-11-22 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Eva_2", "0003_rename_categoria_luchador_categoria"),
    ]

    operations = [
        migrations.CreateModel(
            name="Evento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=200)),
                ("fecha", models.DateField()),
                (
                    "lugar",
                    models.CharField(default="Lugar Desconocido", max_length=200),
                ),
                (
                    "imagen",
                    models.ImageField(blank=True, null=True, upload_to="eventos/"),
                ),
                ("luchadores", models.ManyToManyField(blank=True, to="Eva_2.luchador")),
            ],
        ),
    ]