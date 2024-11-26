# Generated by Django 5.1.3 on 2024-11-26 11:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Kpi",
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
                ("name", models.CharField(max_length=50, unique=True)),
                ("expression", models.CharField(max_length=100)),
                (
                    "description",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="KpiAssitLink",
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
                ("asset_id", models.IntegerField()),
                ("result", models.CharField(max_length=100)),
                (
                    "Kpi_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="kpi.kpi"
                    ),
                ),
            ],
        ),
    ]