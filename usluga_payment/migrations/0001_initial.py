# Generated by Django 4.1.1 on 2022-09-28 12:03

from django.db import migrations, models

import usluga_payment.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Podiezd",
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
                ("account_number", models.IntegerField()),
                ("refill_date_time", models.DateTimeField(auto_now_add=True)),
                (
                    "amount",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("action", models.CharField(max_length=50)),
                (
                    "random_number",
                    models.CharField(
                        default=usluga_payment.utils.create_new_ref_number,
                        max_length=10,
                    ),
                ),
            ],
        ),
    ]
